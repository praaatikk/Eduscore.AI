from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import os


# ------------------- Flask App Configuration -------------------
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super_secret_key_123'

# 🔧 Fix session cookie behavior on localhost (important for login persistence)
app.config['SESSION_COOKIE_SECURE'] = False       # allow cookies without HTTPS
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'     # prevent Chrome blocking local cookies
app.config['SESSION_COOKIE_HTTPONLY'] = True      # protect session cookie from JS access

# Initialize Database
db = SQLAlchemy(app)


# ------------------- Database Model -------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


# ------------------- Home Route -------------------
@app.route('/')
def home():
    # Check if user logged in
    if 'user_id' not in session:
        flash("Please login first!", "warning")
        return redirect(url_for('login'))

    return render_template('home.html')



@app.route('/')
def index():
    return render_template('index.html')



# ------------------- Registration -------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password']

        # ✅ Check if username already exists
        existing_user_by_username = User.query.filter_by(username=username).first()
        if existing_user_by_username:
            flash('Username already taken. Please choose another.', 'danger')
            return redirect(url_for('register'))

        # ✅ Check if email already exists
        existing_user_by_email = User.query.filter_by(email=email).first()
        if existing_user_by_email:
            flash('Email already registered. Please use another.', 'danger')
            return redirect(url_for('register'))

        # ✅ Hash password securely
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # ✅ Try to save user, handle unexpected DB errors gracefully
        try:
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An unexpected error occurred. Please try again.', 'danger')
            print("Error during registration:", e)
            return redirect(url_for('register'))

    return render_template('register.html')

# ------------------- Login -------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # ✅ store session data
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f"Welcome back, {user.username}!", "success")
            return redirect('/')   # redirect to home directly
        else:
            flash("Invalid email or password", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')


# ------------------- Logout -------------------
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))


# ------------------- Prediction -------------------
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if 'user_id' not in session:
        flash("Please login first!", "warning")
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('home.html')

    # Collect data from form
    data = CustomData(
        gender=request.form.get('gender'),
        race_ethnicity=request.form.get('ethnicity'),
        parental_level_of_education=request.form.get('parental_level_of_education'),
        lunch=request.form.get('lunch'),
        test_preparation_course=request.form.get('test_preparation_course'),
        reading_score=float(request.form.get('reading_score')),
        writing_score=float(request.form.get('writing_score'))
    )

    pred_df = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    return render_template('home.html', results=results[0])


# ------------------- App Runner -------------------
if __name__ == '__main__':
    # Create DB if not exists
    if not os.path.exists('app.db'):
        with app.app_context():
            db.create_all()
            print("✅ Database created successfully!")

    # Run the app
    app.run(host='127.0.0.1', port=5000, debug=True)

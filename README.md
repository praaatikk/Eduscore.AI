EduScore.AI — Student Performance Prediction Web App

EduScore.AI is a Flask-based machine learning web application that predicts a student’s final exam performance based on demographic and academic factors such as gender, ethnicity, parental education, lunch type, and test preparation.
It features user authentication, prediction history, and a clean Bootstrap-based UI.




🚀 Features

✅ Machine Learning Integration

Predicts student exam performance using a pre-trained ML model (model.pkl).

✅ User Authentication

Secure registration and login system with hashed passwords.

Session-based login management.

✅ Prediction Dashboard

Users can input details and get instant predicted scores.

Option to view past predictions (if enabled).

✅ Responsive Frontend

Modern Bootstrap 5 interface.

Consistent layout with navigation bar and flash messages.

✅ Persistent Database

SQLite used for storing users and predictions.

Auto-created on first run.




🧠 Tech Stack
Layer	Technology
Frontend	HTML5, CSS3, Bootstrap 5, Jinja2
Backend	Flask (Python)
Database	SQLite
ML Model	scikit-learn (Custom Pipeline)
Security	Werkzeug password hashing
Deployment	Localhost / Render / Railway (optional)



🧩 Project Structure
EduScoreAI/
├── app.py
├── requirements.txt
├── app.db
├── src/
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   ├── model/
│   │   └── model.pkl
│   └── utils/
│       └── __init__.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── home.html
├── static/
│   ├── css/
│   └── images/
└── README.md





⚙️ Installation & Setup
🪶 1. Clone the repository
git clone https://github.com/<praaatikk>/EduScoreAI.git
cd EduScoreAI

📦 2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate   # (on Windows)
# or
source venv/bin/activate   # (on macOS/Linux)

📚 3. Install dependencies
pip install -r requirements.txt

🧱 4. Run the application
python app.py


Then open your browser and go to 👉 http://127.0.0.1:5000






🧮 Usage

Register with your name, email, and password.

Login to access the prediction form.

Enter student data (gender, ethnicity, education level, etc.).

Click Predict to view the estimated score.

Optionally, check your past predictions on the dashboard.



📊 Example Input
Feature	Example Value
Gender	Female
Ethnicity	Group B
Parental Level of Education	Bachelor's Degree
Lunch	Standard
Test Preparation Course	Completed
Reading Score	72
Writing Score	70

✅ Output Example:

Predicted Math Score: 68.4



🔐 Security

Passwords hashed with PBKDF2:SHA256.

Session management for logged-in users.

Protected prediction routes (login required).




💡 Future Enhancements

Add “My Predictions” Dashboard with charts (Plotly/Chart.js).

Enable model retraining using uploaded CSV files.

Implement password reset via email.

Deploy to Render or Railway for live demo.



🧑‍💻 Authors
Name	Role
Pratik Gadekar	Data Scientist and ML Developer


🏁 License

This project is licensed under the MIT License — feel free to modify and use it for educational purposes.



🌟 Screenshots (optional)

You can add these later for presentation marks:

📸 screenshots/
   ├── home.png
   ├── login.png
   ├── register.png
   ├── predict.png
   └── dashboard.png
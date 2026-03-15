# EduScore.AI 🎓
### AI-Powered Student Performance Prediction

EduScore.AI is a full-stack machine learning web application that predicts a student's math score based on demographic and academic inputs. Built with Flask and powered by a trained ML model, it features cloud database storage, a prediction dashboard, and automated email alerts — all deployed live on the web.

---

## 🌐 Live Demo
> Deployed on Render — [Coming Soon]

---

## ✨ Features

### 🤖 Machine Learning Prediction
- Predicts math scores using a pre-trained model trained on 8 algorithms (Linear Regression, XGBoost, CatBoost, Random Forest, and more)
- Automatically selects the best performing model based on R² score
- Inputs: gender, ethnicity, parental education, lunch type, test preparation, reading & writing scores

### ☁️ Cloud Integration (Supabase PostgreSQL)
- All user accounts and prediction history stored in a cloud database
- Data persists across sessions and deployments
- Real-time access from anywhere

### 📊 Prediction Dashboard
- Logged-in users can view their full prediction history
- Summary stats: total predictions, average score, best score
- Color-coded score badges (green / yellow / red)

### 📧 Email Alerts
- Every prediction automatically triggers an email to the teacher
- HTML email includes predicted score, grade label, and input summary
- Powered by Gmail SMTP

### 🔐 User Authentication
- Secure registration and login with PBKDF2:SHA256 password hashing
- Session-based login management
- All prediction routes protected (login required)

### 🎨 Modern UI
- Glassmorphism design with Bootstrap 5
- Responsive layout with navbar, flash messages, and animations
- Consistent theme across all pages

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Bootstrap 5, Jinja2 |
| Backend | Flask (Python) |
| Database | Supabase (PostgreSQL) |
| ML Model | scikit-learn, XGBoost, CatBoost |
| Email | Gmail SMTP |
| Security | Werkzeug password hashing |
| Deployment | Render |

---

## 🧩 Project Structure

```
EduScore.AI/
├── app.py                        # Main Flask app
├── requirements.txt
├── templates/
│   ├── base.html                 # Shared layout + navbar
│   ├── home.html                 # Prediction form
│   ├── dashboard.html            # Prediction history
│   ├── login.html
│   └── register.html
├── src/
│   ├── pipeline/
│   │   └── predict_pipeline.py  # ML prediction logic
│   ├── component/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── artifacts/
│   ├── model.pkl                 # Trained ML model
│   └── preprocessor.pkl          # Data preprocessor
└── notebook/
    ├── EDA STUDENT PERFORMANCE.ipynb
    └── MODEL TRAINING.ipynb
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/praaatikk/EduScoreAI.git
cd EduScoreAI
```

### 2. Create & activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install psycopg2-binary
```

### 4. Configure environment variables
Create a `.env` file or set these directly:
```
DATABASE_URL=postgresql://your_supabase_connection_string
SECRET_KEY=your_secret_key
SENDER_EMAIL=your_gmail@gmail.com
APP_PASSWORD=your_gmail_app_password
```

### 5. Run the application
```bash
python app.py
```
Open your browser → [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧮 Usage

1. **Register** with your name, email, and password
2. **Login** to access the prediction form
3. **Enter student data** — gender, ethnicity, education level, scores
4. **Click Predict** to get the estimated math score instantly
5. **Check Dashboard** to view your full prediction history
6. **Email alert** is automatically sent to the teacher's inbox

---

## 📊 Example

| Feature | Example Value |
|---|---|
| Gender | Female |
| Ethnicity | Group B |
| Parental Education | Bachelor's Degree |
| Lunch | Standard |
| Test Preparation | Completed |
| Reading Score | 72 |
| Writing Score | 70 |

**Output:**
```
🎯 Predicted Math Score: 68.4
```

---

## 🔐 Security

- Passwords hashed with PBKDF2:SHA256
- Session-based authentication
- All sensitive credentials stored as environment variables
- Protected routes — login required for predictions and dashboard

---

## 🧑‍💻 Authors

| Name | Role |
|---|---|
| Pratik Gadekar | ML Developer & Full Stack |

---

## 📄 License

This project is licensed under the MIT License — free to use for educational purposes.

# 📧 SpamDetect AI – Email Spam Classification Web App
### Unlock the power of Machine Learning to detect whether an email is Spam or Not Spam!
### This web application supports single email prediction, bulk classification, user authentication, and a clean UI.

# ✨ Features
## 🔍 Email Classification
### ✔️ Classifies text as Spam / Not Spam

### ✔️ Displays prediction confidence score

### ✔️ Supports CSV, TXT, XLSX files for bulk detection

### ✔️ Preprocesses text intelligently

# 🔐 User Authentication
### Register new users

### Login with username/email

### Secure password hashing

### Logout functionality

### Route protection (non‑logged users cannot access the main app)

### Stores all user info securely in SQLite database

# 🗂 Bulk File Classification
### Upload large datasets

### Cleans and extracts meaningful text

### Auto‑detects file encoding

### Shows results in a clean HTML table

# 🛠 Additional Features
### Debug logs for troubleshooting

### Error handling for invalid file types

### Smooth session management

# 🧠 Technologies Used
## 🔹 Backend
### Python (Flask Framework)

### SQLite Database

### Werkzeug Security

### Pickle (for ML model loading)

### Pandas for file handling

##🔹 Machine Learning
### TF‑IDF Vectorizer

### Logistic Regression (or your trained ML model)

### Text preprocessing & normalization

##🔹 Frontend
### HTML

### CSS

### Jinja2 Templates

##🔹 Other Tools
### dotenv for secret key

### Session management

# 🚀 How to Use
### Register or Login to access the system

## From the dashboard:

### 📝 Enter email text → Get prediction

### 📂 Upload a file → See spam analysis

### View results in a clean, easy‑to‑read table

Logout securely when done


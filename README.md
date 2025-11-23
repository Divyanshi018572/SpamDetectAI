
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
### 1. Register new users

### 2. Login with username/email

### 3. Secure password hashing

### 4.Logout functionality

### 5.Route protection (non‑logged users cannot access the main app)

### 6. Stores all user info securely in SQLite database

# 🗂 Bulk File Classification
### 1. Upload large datasets

### 2. Cleans and extracts meaningful text

### 3. Auto‑detects file encoding

### 4. Shows results in a clean HTML table

# 🛠 Additional Features
### 1. Debug logs for troubleshooting

### 2. Error handling for invalid file types

### 3. Smooth session management

# 🧠 Technologies Used
## 🔹 Backend
### 1. Python (Flask Framework)

### 2. SQLite Database

### 3. Werkzeug Security

### 4. Pickle (for ML model loading)

### 5. Pandas for file handling

## 🔹 Machine Learning
### 1. TF‑IDF Vectorizer

### 2. Logistic Regression (or your trained ML model)

### 4. Naive Bayes Algorithm (MultinomicalNB, BernoulliNB, GaussianNB)

### 3. Text preprocessing & normalization

## 🔹 Frontend
### HTML

### CSS

### Jinja2 Templates

## 🔹 Other Tools
### dotenv for secret key

### Session management

# 🚀 How to Use
### Register or Login to access the system

## From the dashboard:

### 📝 Enter email text → Get prediction

### 📂 Upload a file → See spam analysis

### View results in a clean, easy‑to‑read table




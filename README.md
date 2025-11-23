📧 SpamDetect AI – Email Spam Classification Web App
An intelligent web application that detects whether an email is Spam or Not Spam using Machine Learning (ML).
It provides single email prediction, bulk file classification, and a secure login/register system.

🚀 What This Project Does
✔️ Classifies email text as Spam or Not Spam
✔️ Shows prediction confidence score
✔️ Supports file uploads for bulk classification
✔️ Handles CSV, TXT, XLSX formats
✔️ Provides user authentication:

🔐 Register

🔐 Login

🔐 Logout
✔️ Stores user information securely in SQLite database
✔️ Protects routes so only logged-in users can access the main app
✔️ Clean & user‑friendly UI built with HTML/CSS + Flask templates

🧠 Technologies Used
🔹 Backend
Python (Flask Framework)

SQLite Database for user storage

Werkzeug Security for password hashing

Pickle for loading trained ML model

Pandas for file processing

🔹 Machine Learning
TF‑IDF Vectorizer

Logistic Regression (or your trained model)

Preprocessing using text normalization

🔹 Frontend
HTML | CSS | Jinja2 Templates

Forms for login, registration & file upload

🔹 Other Tools
dotenv for secret key management

Session Management for authentication

Error handling & file validation

Debug logs for smooth troubleshooting


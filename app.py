import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, url_for, redirect,g,session
import pickle
import pandas as pd


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
from auth import auth
app.register_blueprint(auth)


# Load model and vectorizer
tfidf = pickle.load(open('vectorize.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Text preprocessing function
def transform_text(text):
    return text.lower()


@app.route('/')
def home():
    print("DEBUG session:", dict(session))
    print("DEBUG g.user:", g.user)

    if g.user is None:
        return redirect(url_for('auth.login'))

    return render_template('index.html', user=g.user)



from functools import wraps

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return wrapper



# ............ SINGLE EMAIL PREDICTION ...............
@app.route('/predict', methods=['POST'])
def predict():
    email = request.form['email']
    transformed = transform_text(email)
    vector_input = tfidf.transform([transformed])
    result = model.predict(vector_input)[0]
    proba = model.predict_proba(vector_input)[0][1] * 100

    return render_template('index.html',
                           prediction=('Spam' if result == 1 else 'Not Spam'),
                           confidence=round(proba, 2))

# ........FILE UPLOAD PREDICTION.........

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file or file.filename == '':
        return "No file uploaded.", 400

    filename = file.filename.lower()
    try:
        if filename.endswith('.csv'):
            try:
                file.seek(0)
                df = pd.read_csv(file)
            except Exception:
                file.seek(0)
                df = pd.read_csv(file, encoding='latin1', errors='ignore')
        elif filename.endswith('.xlsx'):
            file.seek(0)
            try:
                df = pd.read_excel(file)
            except Exception:
                return "Error reading Excel file. Please upload a valid .xlsx file.", 400

        elif filename.endswith('.txt'):
            file.seek(0)
            raw_bytes = file.read()

            # Remove null bytes that break decoding (common in UTF-16)
            cleaned_bytes = raw_bytes.replace(b'\x00', b'')

            # Try decoding in multiple encodings
            for enc in ['utf-8', 'latin1', 'utf-16', 'utf-32']:
                try:
                    raw_text = cleaned_bytes.decode(enc)
                    break
                except:
                    raw_text = None
                    continue

            if raw_text is None:
                return "Could not decode TXT file. Try saving it as UTF-8.", 400

            # Split into non-empty lines
            lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

            print("DEBUG Lines:", lines[:5])  # show first 5

            if not lines:
                return "TXT file has no usable text lines. Try re-saving the file as UTF-8.", 400

            df = pd.DataFrame({'text': lines})




        else:
            return "Unsupported file format. Please upload CSV, XLSX, or TXT.", 400

        print("DEBUG: df shape after load:", getattr(df, "shape", None))
        print("DEBUG: df columns:", list(df.columns))

        if df is None or df.shape[0] == 0:
            return "Uploaded file has no rows.", 400

        # find text column if needed
        possible_cols = ['text', 'message', 'email', 'content', 'body']
        found = None
        for c in possible_cols:
            if c in df.columns:
                found = c
                break
        if found is None:
            if df.shape[1] == 1:
                found = df.columns[0]
                print(f"DEBUG: Using single column '{found}' as text.")
            else:
                return ("No text column found. Use column named 'text' or upload a single-column file."), 400

        df = df.copy()
        df['text'] = df[found].astype(str).str.strip()
        df = df[df['text'].str.len() > 0].reset_index(drop=True)
        print("DEBUG: rows after dropping blanks:", df.shape[0])
        if df.shape[0] == 0:
            return "No valid (non-empty) text rows after cleaning.", 400

        df['transformed'] = df['text'].astype(str).apply(transform_text)

        df = df[df['transformed'].str.len() > 0].reset_index(drop=True)
        print("DEBUG: rows after transform_text:", df.shape[0])
        if df.shape[0] == 0:
            return ("All messages empty after preprocessing. Try simplifying transform_text() temporarily."), 400

        X = tfidf.transform(df['transformed'])
        preds = model.predict(X)
        probs = model.predict_proba(X)[:, 1] * 100
        df['prediction'] = ['Spam' if p == 1 else 'Not Spam' for p in preds]
        df['confidence'] = probs.round(2)

        return render_template('result.html', tables=[df.to_html(classes='data', index=False, border=0)])

    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error processing file: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)




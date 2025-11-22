# auth.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'users.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

# Ensure DB exists on import
init_db()


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
        return

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, username, email FROM users WHERE id = ?",
        (user_id,)
    )
    g.user = cur.fetchone()
    conn.close()



@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')

        if not username or not email or not password:
            flash('Please fill all fields.', 'warning')
            return render_template('register.html')

        if password != confirm:
            flash('Passwords do not match.', 'warning')
            return render_template('register.html')

        password_hash = generate_password_hash(password)

        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                        (username, email, password_hash))
            conn.commit()
            conn.close()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists.', 'danger')
            return render_template('register.html')

    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_username = request.form.get('email_or_username', '').strip()
        password = request.form.get('password', '')

        conn = get_db()
        cur = conn.cursor()
        # allow login by username or email
        cur.execute("SELECT id, username, email, password_hash FROM users WHERE email = ? OR username = ?",
                    (email_or_username.lower(), email_or_username))
        user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            session.clear()
            session['user_id'] = user['id']
            flash(f"Welcome back, {user['username']}!", 'success')
            # redirect to home or to next
            next_url = request.args.get('next') or url_for('home')
            return redirect(next_url)
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            return render_template('login.html')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 2525))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
REPLY_TO = os.getenv("REPLY_TO")
DB_PATH = os.getenv("DB_PATH")

app = Flask(__name__, static_url_path='/happy-birthday/static')

app.secret_key = os.getenv('FLASK_SECRET_KEY')

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS birthdays (
            email TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            dob TEXT NOT NULL
        )''')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.execute("SELECT dob FROM birthdays WHERE email = ?", (email,))
            existing = cursor.fetchone()

            if existing:
                conn.execute("UPDATE birthdays SET name = ?, dob = ? WHERE email = ?", (name, dob, email))
                flash("Birthday and/or name updated successfully")
                subject = "LSK Birthday Emailer: Entry Updated"
                content = "updated their info"
            else:
                conn.execute("INSERT INTO birthdays (email, name, dob) VALUES (?, ?, ?)", (email, name, dob))
                flash("Sign up successful")
                subject = "LSK Birthday Emailer: New Entry"
                content = "signed up"
                
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = SENDER_EMAIL
            msg['To'] = REPLY_TO
            msg.set_content(f"A user has {content}:\n\nName: {name}\nEmail: {email}\nBirthday: {dob}")
                
            try:
                smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                smtp.starttls()
                smtp.login(SMTP_USER, SMTP_PASS)
                smtp.send_message(msg)
                smtp.quit()
            except Exception as e:
                print(f"Failed to send notification: {e}")
        
        return redirect(url_for('index'))
    
    return render_template('form.html')

if __name__ == '__main__':
    init_db()
    app.run('127.0.0.1', 5001, debug=True)
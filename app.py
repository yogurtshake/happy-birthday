from flask import Flask, render_template, request, redirect, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'
DB_PATH = 'birthdays.db'

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
                flash("Birthday updated successfully")
            else:
                conn.execute("INSERT INTO birthdays (email, name, dob) VALUES (?, ?, ?)", (email, name, dob))
                flash("Sign up successful")

        return redirect('/')
    
    return render_template('form.html')

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=5001)
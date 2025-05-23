from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_PATH = 'birthdays.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS birthdays (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            dob TEXT NOT NULL
        )''')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        dob = request.form['dob']
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("INSERT INTO birthdays (email, dob) VALUES (?, ?)", (email, dob))
        return redirect('/')
    return render_template('form.html')

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=5001)

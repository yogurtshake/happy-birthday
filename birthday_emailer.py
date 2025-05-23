import sqlite3
from datetime import datetime
import subprocess

DB_PATH = '/home/YOUR_USER/birthday-app/birthdays.db'
TODAY = datetime.today().strftime('%m-%d')

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.execute("SELECT email, dob FROM birthdays")
    for email, dob in cursor.fetchall():
        if dob[5:] == TODAY:
            subject = "Happy Birthday!"
            body = "Wishing you a fantastic birthday 🎉!"
            subprocess.run(['mail', '-s', subject, email], input=body.encode())

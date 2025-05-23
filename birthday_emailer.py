import sqlite3
from datetime import datetime
import subprocess

DB_PATH = 'birthdays.db'
TODAY = datetime.today().strftime('%m-%d')

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.execute("SELECT name, email, dob FROM birthdays")
    for name, email, dob in cursor.fetchall():
        if dob[5:] == TODAY:
            subject = "Happy Birthday!"
            body = (
                f"Dear {name},\n\n"
                "Happy Birthday. Hope you have a good one."
                "\n\nSincerely,\nLucas' Birthday Emailer"
                "\nbirthday.lucas.su-keun.kim"
            )
            subprocess.run(
                ['mail', '-s', subject, '-a', 'Reply-To: lucassukeunkim@gmail.com', '-c', 'lucassukeunkim@gmail.com', email],
                input=body.encode()
            )

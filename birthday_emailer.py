import sqlite3
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

DB_PATH = '/home/lskyogurtshake/happy-birthday/birthdays.db'

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 2525))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
REPLY_TO = os.getenv("REPLY_TO")


def send_birthday_email(name, to_email):
    msg = EmailMessage()
    msg['Subject'] = "Happy Birthday!"
    msg['From'] = f"Lucas Kim <{SENDER_EMAIL}>"
    msg['To'] = to_email
    msg['Reply-To'] = REPLY_TO
    msg.set_content(f"""Dear {name},

Happy Birthday! Hope you have a good one.

Sincerely,
Lucas


**This is an automated message sent from my server. 
If you want to unsubscribe, reply and let me know.**

https://birthday.lucas.su-keun.kim
""")

    bcc_address = REPLY_TO
    recipients = [to_email, bcc_address]

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg, to_addrs=recipients)
        print(f"Sent birthday email to {name} <{to_email}>")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def main():
    today = datetime.today().strftime('%m-%d')
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT name, email, dob FROM birthdays")
        for name, email, dob in cursor.fetchall():
            if dob[5:] == today:
                send_birthday_email(name, email)

if __name__ == "__main__":
    main()

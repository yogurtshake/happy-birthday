import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

DB_PATH = os.getenv("DB_PATH")
email_to_delete = input("Enter email to delete: ").strip()

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM birthdays WHERE email = ?", (email_to_delete,))
    conn.commit()

    print(f"Deleted rows with email: {email_to_delete}")

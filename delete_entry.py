import sqlite3

email_to_delete = input("Enter email to delete: ").strip()

with sqlite3.connect("birthdays.db") as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM birthdays WHERE email = ?", (email_to_delete,))
    conn.commit()

    print(f"Deleted rows with email: {email_to_delete}")

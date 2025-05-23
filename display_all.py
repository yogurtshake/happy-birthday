import sqlite3

DB_PATH = 'birthdays.db'

def print_birthdays():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT email, name, dob FROM birthdays")
        rows = cursor.fetchall()

        if not rows:
            print("Nothing found in the database.")
            return

        print(f"{'Email':<30} {'Name':<20} {'Date of Birth'}")
        print("-" * 65)
        for email, name, dob in rows:
            print(f"{email:<30} {name:<20} {dob}")

if __name__ == '__main__':
    print_birthdays()

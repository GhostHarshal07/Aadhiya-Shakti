import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)
cur = con.cursor()


def insert_record():
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    cur.execute("INSERT INTO student(name, email, age) VALUES(%s, %s, %s)", (name, email, age))
    con.commit()
    print("Record inserted successfully")


def display_records():
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    if not rows:
        print("No records found")
        return
    print(f"{'ID':<5}{'Name':<20}{'Email':<30}{'Age':<5}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<20}{row[2]:<30}{row[3]:<5}")


def search_record():
    sid = int(input("Enter ID to search: "))
    cur.execute("SELECT * FROM student WHERE id=%s", (sid,))
    row = cur.fetchone()
    if row:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Email:", row[2])
        print("Age:", row[3])
    else:
        print("Record not found")


def update_record():
    sid = int(input("Enter ID to update: "))
    cur.execute("SELECT * FROM student WHERE id=%s", (sid,))
    if not cur.fetchone():
        print("Record not found")
        return
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    age = int(input("Enter new age: "))
    cur.execute("UPDATE student SET name=%s, email=%s, age=%s WHERE id=%s", (name, email, age, sid))
    con.commit()
    print("Record updated successfully")


def delete_record():
    sid = int(input("Enter ID to delete: "))
    cur.execute("DELETE FROM student WHERE id=%s", (sid,))
    con.commit()
    if cur.rowcount > 0:
        print("Record deleted successfully")
    else:
        print("Record not found")


while True:
    print("\n===== STUDENT MENU =====")
    print("1. Insert Record")
    print("2. Display Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            insert_record()
        elif choice == "2":
            display_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            update_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input, please enter numbers where required")

cur.close()
con.close()

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)
cur = con.cursor()

cur.execute("INSERT INTO student(name, email, age) VALUES(%s, %s, %s)", ("Rahul", "rahul@gmail.com", 21))
cur.execute("INSERT INTO student(name, email, age) VALUES(%s, %s, %s)", ("Priya", "priya@gmail.com", 22))
con.commit()
print("Records inserted")

cur.execute("SELECT * FROM student")
print("\nAll Records:")
for row in cur.fetchall():
    print(row)

cur.execute("UPDATE student SET age=%s WHERE name=%s", (25, "Rahul"))
con.commit()
print("\nRecord updated")

cur.execute("SELECT * FROM student")
print("\nAfter Update:")
for row in cur.fetchall():
    print(row)

cur.execute("DELETE FROM student WHERE name=%s", ("Priya",))
con.commit()
print("\nRecord deleted")

cur.execute("SELECT * FROM student")
print("\nAfter Delete:")
for row in cur.fetchall():
    print(row)

cur.close()
con.close()

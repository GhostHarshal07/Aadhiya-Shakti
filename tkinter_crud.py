import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testdb"
    )


def load_data():
    for row in tree.get_children():
        tree.delete(row)
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)
    cur.close()
    con.close()


def clear_fields():
    id_var.set("")
    name_var.set("")
    email_var.set("")
    age_var.set("")


def add_record():
    name = name_var.get().strip()
    email = email_var.get().strip()
    age = age_var.get().strip()
    if not name or not email or not age:
        messagebox.showwarning("Warning", "All fields are required")
        return
    if not age.isdigit():
        messagebox.showwarning("Warning", "Age must be a number")
        return
    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO student(name, email, age) VALUES(%s, %s, %s)", (name, email, int(age)))
    con.commit()
    cur.close()
    con.close()
    messagebox.showinfo("Success", "Record added")
    clear_fields()
    load_data()


def update_record():
    sid = id_var.get()
    if not sid:
        messagebox.showwarning("Warning", "Select a record to update")
        return
    name = name_var.get().strip()
    email = email_var.get().strip()
    age = age_var.get().strip()
    if not name or not email or not age.isdigit():
        messagebox.showwarning("Warning", "Enter valid data")
        return
    con = get_connection()
    cur = con.cursor()
    cur.execute("UPDATE student SET name=%s, email=%s, age=%s WHERE id=%s", (name, email, int(age), int(sid)))
    con.commit()
    cur.close()
    con.close()
    messagebox.showinfo("Success", "Record updated")
    clear_fields()
    load_data()


def delete_record():
    sid = id_var.get()
    if not sid:
        messagebox.showwarning("Warning", "Select a record to delete")
        return
    if not messagebox.askyesno("Confirm", "Delete this record?"):
        return
    con = get_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=%s", (int(sid),))
    con.commit()
    cur.close()
    con.close()
    messagebox.showinfo("Success", "Record deleted")
    clear_fields()
    load_data()


def on_select(event):
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")
    id_var.set(values[0])
    name_var.set(values[1])
    email_var.set(values[2])
    age_var.set(values[3])


root = tk.Tk()
root.title("Student CRUD")
root.geometry("650x450")

id_var = tk.StringVar()
name_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.StringVar()

form = tk.Frame(root, padx=10, pady=10)
form.pack(fill=tk.X)

tk.Label(form, text="ID").grid(row=0, column=0, sticky="w", pady=3)
tk.Entry(form, textvariable=id_var, state="readonly", width=30).grid(row=0, column=1, pady=3)
tk.Label(form, text="Name").grid(row=1, column=0, sticky="w", pady=3)
tk.Entry(form, textvariable=name_var, width=30).grid(row=1, column=1, pady=3)
tk.Label(form, text="Email").grid(row=2, column=0, sticky="w", pady=3)
tk.Entry(form, textvariable=email_var, width=30).grid(row=2, column=1, pady=3)
tk.Label(form, text="Age").grid(row=3, column=0, sticky="w", pady=3)
tk.Entry(form, textvariable=age_var, width=30).grid(row=3, column=1, pady=3)

buttons = tk.Frame(root, padx=10)
buttons.pack(fill=tk.X)

tk.Button(buttons, text="Add", width=10, command=add_record).pack(side=tk.LEFT, padx=5)
tk.Button(buttons, text="Update", width=10, command=update_record).pack(side=tk.LEFT, padx=5)
tk.Button(buttons, text="Delete", width=10, command=delete_record).pack(side=tk.LEFT, padx=5)
tk.Button(buttons, text="Clear", width=10, command=clear_fields).pack(side=tk.LEFT, padx=5)

tree = ttk.Treeview(root, columns=("ID", "Name", "Email", "Age"), show="headings")
for col in ("ID", "Name", "Email", "Age"):
    tree.heading(col, text=col)
tree.column("ID", width=50)
tree.column("Name", width=150)
tree.column("Email", width=250)
tree.column("Age", width=60)
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", on_select)

load_data()
root.mainloop()

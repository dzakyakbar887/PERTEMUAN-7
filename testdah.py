import tkinter as tk
import sqlite3
from tkinter import messagebox


top = tk.Tk()
top.title("my tkinter window")
top.geometry("400x300")
top.configure(bg="blue")
e1 = tk.Entry(top, bd=5)
e1.pack()
e2 = tk.Entry(top, bd=5)
e2.pack()
def simpandata():
    nama = e1.get()
    umur = e2.get()
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("create table if not exists students (id integer primary key autoincrement, nama text, umur integer)")
    cur.execute("insert into students(nama, umur) values(?,?)", (nama, umur))
    con.commit()
    con.close()
    messagebox.showinfo("info", "data berhasil disimpan")

btn = tk.Button(top, text="Simpan", command=simpandata)
btn.pack()
top.mainloop()
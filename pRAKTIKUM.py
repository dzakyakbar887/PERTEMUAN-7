
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Membuat database SQLite
conn = sqlite3.connect("nilai_siswa.db")
cursor = conn.cursor()

# Membuat tabel nilai_siswa
cursor.execute("""
CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_siswa TEXT NOT NULL,
    biologi REAL NOT NULL,
    fisika REAL NOT NULL,
    inggris REAL NOT NULL,
    prediksi_fakultas TEXT NOT NULL
)
""")
conn.commit()



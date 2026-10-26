
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


# Fungsi prediksi dan penyimpanan data
def submit_nilai():
    nama = entry_nama.get().strip()

    try:
        biologi = float(entry_biologi.get())
        fisika = float(entry_fisika.get())
        inggris = float(entry_inggris.get())

        if not nama:
            messagebox.showwarning("Peringatan", "Nama siswa harus diisi!")
            return

        if not all(0 <= n <= 100 for n in [biologi, fisika, inggris]):
            messagebox.showwarning(
                "Peringatan", "Nilai harus antara 0 sampai 100!"
            )
            return

        
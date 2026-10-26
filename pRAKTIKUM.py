
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

        if biologi > fisika and biologi > inggris:
            prediksi = "Kedokteran"
        elif fisika > biologi and fisika > inggris:
            prediksi = "Teknik"
        elif inggris > biologi and inggris > fisika:
            prediksi = "Bahasa"
        else:
            prediksi = "Nilai tertinggi seri"

        cursor.execute("""
            INSERT INTO nilai_siswa
            (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """, (nama, biologi, fisika, inggris, prediksi))

        conn.commit()

        label_hasil.config(text=f"Hasil Prediksi: {prediksi}")
        messagebox.showinfo("Berhasil", "Data berhasil disimpan!")

        entry_nama.delete(0, tk.END)
        entry_biologi.delete(0, tk.END)
        entry_fisika.delete(0, tk.END)
        entry_inggris.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Error", "Masukkan nilai berupa angka yang valid!"
        )


# Membuat tampilan Tkinter
root = tk.Tk()
root.title("Prediksi Fakultas Siswa")
root.geometry("400x430")
root.configure(padx=20, pady=20)

tk.Label(root, text="PREDIKSI FAKULTAS SISWA",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Nama Siswa").pack(anchor="w")
entry_nama = tk.Entry(root, width=35)
entry_nama.pack(pady=5)

tk.Label(root, text="Nilai Biologi").pack(anchor="w")
entry_biologi = tk.Entry(root, width=35)
entry_biologi.pack(pady=5)

tk.Label(root, text="Nilai Fisika").pack(anchor="w")
entry_fisika = tk.Entry(root, width=35)
entry_fisika.pack(pady=5)

tk.Label(root, text="Nilai Inggris").pack(anchor="w")
entry_inggris = tk.Entry(root, width=35)
entry_inggris.pack(pady=5)

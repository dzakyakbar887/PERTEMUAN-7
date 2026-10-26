
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Membuat database SQLite
conn = sqlite3.connect("nilai_siswa.db")
cursor = conn.cursor()


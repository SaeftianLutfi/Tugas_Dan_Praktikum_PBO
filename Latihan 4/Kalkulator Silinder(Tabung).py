import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
import math
from FUNGSI import Luas_Permukaan_Tabung, Volume_Tabung

def Hitung():
    Luas_Permukaan_Tabung(txtr, txtTinggi, txtLuas_Permukaan_Tabung)
    Volume_Tabung(txtr, txtTinggi, txtVolume_Tabung)

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Silinder (Tabung)")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari-Jari
JariJari = Label(frame, text="Jari-jari:")
JariJari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Textbox Jari-Jari
txtr = Entry(frame)
txtr.grid(row=0, column=1)

# Textbox Tinggi
txtTinggi = Entry(frame)
txtTinggi.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Permukaan_Tabung = Entry(frame)
txtLuas_Permukaan_Tabung.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume_Tabung = Entry(frame)
txtVolume_Tabung.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
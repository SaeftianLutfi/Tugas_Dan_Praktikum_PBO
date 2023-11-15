import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
import math
from FUNGSI import Garis_Pelukis, Luas_Kerucut, Volume_Kerucut

def Hitung():
    Garis_Pelukis(txtr, txtTinggi, txtGaris_Pelukis)
    Luas_Kerucut(txtr, txtGaris_Pelukis, txtLuas_Kerucut)
    Volume_Kerucut(txtr, txtTinggi, txtVolume_Kerucut)

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Kerucut")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari-jari
JariJari = Label(frame, text="Jari-Jari:")
JariJari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Textbox Jari-jari
txtr = Entry(frame)
txtr.grid(row=0, column=1)

# Textbox Tinggi
txtTinggi = Entry(frame)
txtTinggi.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Garis Pelukis Kerucut
GarisPelukis = Label(frame, text="Garis Pelukis:")
GarisPelukis.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Garis Pelukis Kerucut
txtGaris_Pelukis = Entry(frame)
txtGaris_Pelukis.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Kerucut = Entry(frame)
txtLuas_Kerucut.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume_Kerucut = Entry(frame)
txtVolume_Kerucut.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
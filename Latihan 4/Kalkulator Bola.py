import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
import math
from FUNGSI import Luas_Bola, Volume_Bola

def Hitung():
    Luas_Bola(txtr, txtLuas_Bola)
    Volume_Bola(txtr, txtVolume_Bola)

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Bola")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari-jari
JariJari = Label(frame, text="Jari-Jari:")
JariJari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Textbox Jari-jari
txtr = Entry(frame)
txtr.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Bola = Entry(frame)
txtLuas_Bola.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume_Bola = Entry(frame)
txtVolume_Bola.grid(row=3, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
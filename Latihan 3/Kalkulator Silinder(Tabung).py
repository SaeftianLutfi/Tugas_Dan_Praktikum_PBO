import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
import math

def hitung_luas_permukaan():
    r = float(txtJariJari.get())
    t = float(txttinggi.get())

    L =2 * math.pi * r * (r + t)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtJariJari.get())
    t = float (txttinggi.get())

    V = math.pi * r ** 2 * t

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas_permukaan()
    hitung_volume()

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
txtJariJari = Entry(frame)
txtJariJari.grid(row=0, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
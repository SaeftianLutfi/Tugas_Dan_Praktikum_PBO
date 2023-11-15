import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
import math

def hitung_garis_pelukis():
    r = float (txtJariJari.get())
    tg = float (txttinggi.get())

    S = math.sqrt(r ** 2 + tg ** 2)

    txtGarisPelukis.delete(0,END)
    txtGarisPelukis.insert(END,S)

def hitung_luas_permukaan():
    r = float(txtJariJari.get())
    S = float(txtGarisPelukis.get())

    L = math.pi * r * (r*S)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtJariJari.get())
    tg = float(txttinggi.get())

    V = (1/3) * math.pi * r ** 2 * tg

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_garis_pelukis()
    hitung_luas_permukaan()
    hitung_volume()

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
txtJariJari = Entry(frame)
txtJariJari.grid(row=0, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
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
txtGarisPelukis = Entry(frame)
txtGarisPelukis.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
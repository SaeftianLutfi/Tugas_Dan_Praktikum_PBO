import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
import math

def hitung_garis_pelukis():
    r = float (txtJariJari.get())
    tg = float (txttinggi.get())

    S = math.sqrt(r ** 2 + tg ** 2)

    txtGarisPelukis.delete(0,END)
    txtGarisPelukis.insert(END,S)

def hitung_luas():
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
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Kerucut")

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

# Output Label Luas Kerucut
luas = Label(frame, text="Luas Kerucut:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume Kerucut
volume = Label(frame, text="Volume Kerucut:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Garis Pelukis Kerucut
txtGarisPelukis = Entry(frame)
txtGarisPelukis.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan Kerucut
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume Kerucut
txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Nama, NIM dan Kelas
nametag = Frame(frame, bg="lightblue", height=30)
nametag.grid(row=6, column=0, columnspan=3, sticky="ew", pady=10)

nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
nama.grid(row=6, column=0, sticky='e', padx=5, pady=5)

nim = Label(nametag, text="220511078", bg='lightblue')
nim.grid(row=6, column=2, sticky="e", padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue') 
kelas.grid(row=6, column=3, sticky='e', padx=5, pady=5)

app.mainloop()
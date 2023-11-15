import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W

def hitung_luas_permukaan():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())

    L = 2 * (p * l + p * t + l * t)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    p = float(txtpanjang.get())
    l = float(txttinggi.get())
    t = float (txttinggi.get())

    V = p * l * t

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Balok")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang
Panjang = Label(frame, text="Panjang:")
Panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label lebar
Lebar = Label (frame, text="Lebar:")
Lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Textbox Panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)

#Textbox lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
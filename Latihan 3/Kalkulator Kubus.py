import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W

def hitung_luas_permukaan():
    s = float(txtsisi.get())

    L = 6 * s **2

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    s = float(txtsisi.get())

    V = s ** 3

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Kubus")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Sisi
Sisi = Label(frame, text="Sisi:")
Sisi.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Textbox Sisi
txtsisi = Entry(frame)
txtsisi.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas = Entry(frame)
txtLuas.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=3, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
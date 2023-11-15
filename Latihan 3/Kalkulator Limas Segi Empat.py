import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W

def hitung_luas_permukaan():
    P = float(txtPanjang.get())
    Lb = float(txtLebar.get())
    TA = float (txtTinggiAlas.get())

    L = P * Lb + 2 * P * TA + 2 * Lb * TA

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    P = float (txtPanjang.get())
    Lb = float (txtLebar.get())
    T = float (txtTinggi.get())
    
    V = (1/3) * P * Lb * T

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Limas Segiempat")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang Alas
Panjang = Label(frame, text="Panjang Alas:")
Panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Lebar Alas
Lebar = Label(frame, text="Lebar Alas:")
Lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
Tinggi = Label(frame, text="Tinggi:")
Tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi Alas
TinggiAlas = Label(frame, text="Tinggi Alas:")
TinggiAlas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#Textbox Panjang Alas
txtPanjang = Entry(frame)
txtPanjang.grid(row=0, column=1)

#Textbox Lebar Alas
txtLebar = Entry(frame)
txtLebar.grid(row=1, column=1)

# Textbox Tinggi
txtTinggi = Entry(frame)
txtTinggi.grid(row=2, column=1)

# Textbox Tinggi Alas
txtTinggiAlas = Entry(frame)
txtTinggiAlas.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
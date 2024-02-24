import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W

def hitung_luas():
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
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Balok")

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

# Output Label Luas Balok
luas = Label(frame, text="Luas Balok:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume Balok
volume = Label(frame, text="Volume Balok:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Balok
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume Balok
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
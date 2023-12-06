import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W

def hitung_luas():
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
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Limas Segiempat")

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

# Output Label Luas Limas SegiEmpat
luas = Label(frame, text="Luas Limas Segiempat:")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume Limas SegiEmpat
volume = Label(frame, text="Volume Limas SegiEmpat:")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Limas SegiEmpat
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume Limas SegiEmpat
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Nama, NIM dan Kelas
nametag = Frame(frame, bg="lightblue", height=30)
nametag.grid(row=7, column=0, columnspan=3, sticky="ew", pady=10)

nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
nama.grid(row=7, column=0, sticky='e', padx=5, pady=5)

nim = Label(nametag, text="220511078", bg='lightblue')
nim.grid(row=7, column=2, sticky="e", padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue') 
kelas.grid(row=7, column=3, sticky='e', padx=5, pady=5)

app.mainloop()
import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
from FUNGSI import Luas_Limas_Segiempat, Volume_Limas_Segiempat

def Hitung():
    Luas_Limas_Segiempat(txtPanjang, txtLebar, txtTinggi_alas, txtLuas_Limas_Segiempat)
    Volume_Limas_Segiempat(txtPanjang, txtLebar, txtTinggi, txtVolume_Limas_Segiempat)

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

# Label Tinggi Alas
Tinggi_Alas = Label(frame, text="Tinggi Alas:")
Tinggi_Alas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

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
txtTinggi_alas = Entry(frame)
txtTinggi_alas.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Limas SegiEmpat
luas = Label(frame, text="Luas Limas SegiEmpat:")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume Limas SegiEmpat
volume = Label(frame, text="Volume Limas SegiEmpat:")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Limas SegiEmpat
txtLuas_Limas_Segiempat = Entry(frame)
txtLuas_Limas_Segiempat.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume Limas SegiEmpat
txtVolume_Limas_Segiempat = Entry(frame)
txtVolume_Limas_Segiempat.grid(row=6, column=1, sticky=W, padx=5, pady=5)

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
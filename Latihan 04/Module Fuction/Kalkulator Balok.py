import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
from FUNGSI import Luas_Balok, Volume_Balok

def Hitung():
    Luas_Balok(txtPanjang, txtLebar, txtTinggi, txtLuas_Balok)
    Volume_Balok(txtPanjang,txtLebar,txtTinggi, txtVolume_Balok)
    
# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Balok")

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
txtPanjang = Entry(frame)
txtPanjang.grid(row=0, column=1)

#Textbox lebar
txtLebar = Entry(frame)
txtLebar.grid(row=1, column=1)

# Textbox Tinggi
txtTinggi = Entry(frame)
txtTinggi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Balok
luas = Label(frame, text="Luas Balok:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume Balok
volume = Label(frame, text="Volume Balok:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Balok
txtLuas_Balok = Entry(frame)
txtLuas_Balok.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume Balok
txtVolume_Balok = Entry(frame)
txtVolume_Balok.grid(row=5, column=1, sticky=W, padx=5, pady=5)

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
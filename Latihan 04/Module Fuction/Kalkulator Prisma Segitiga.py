import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
from FUNGSI import Luas_Segitiga, Keliling_Segitiga, Luas_Permukaan_Prisma_Segitiga, Volume_Prisma_Segitiga

def Hitung():
    Luas_Segitiga(txtPanjang, txtTinggi_Segitiga_Dasar, txtLuas_Segitiga)
    Keliling_Segitiga(txtPanjang, txtKeliling_Segitiga)
    Luas_Permukaan_Prisma_Segitiga(txtLuas_Segitiga, txtKeliling_Segitiga, txtTinggi_Prisma, txtLuas_Permukaan_Prisma_Segitiga)
    Volume_Prisma_Segitiga(txtLuas_Segitiga, txtTinggi_Prisma, txtVolume_Prisma_Segitiga)

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Prisma Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang Sisi Segitiga Dasar
Panjang = Label(frame, text="Panjang Sisi Segitiga Dasar:")
Panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Segitiga Dasar
TinggiSegitigaDasar = Label(frame, text="Tinggi Segitiga Dasar:")
TinggiSegitigaDasar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Prisma
TinggiPrisma = Label(frame, text="Tinggi Prisma:")
TinggiPrisma.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Textbox Panjang Sisi Segitiga Dasar
txtPanjang = Entry(frame)
txtPanjang.grid(row=0, column=1)

#Textbox Tinggi Segitiga Dasar
txtTinggi_Segitiga_Dasar = Entry(frame)
txtTinggi_Segitiga_Dasar.grid(row=1, column=1)

# Textbox Tinggi Prisma
txtTinggi_Prisma = Entry(frame)
txtTinggi_Prisma.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Segitiga
LuasSegitiga = Label(frame, text="Luas Segitiga:")
LuasSegitiga.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Keliling Segitiga
KelilingSegitiga = Label(frame, text="Keliling Segitiga:")
KelilingSegitiga.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Prisma Segitiga
luas = Label(frame, text="Luas Prisma Segitiga:")
luas.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume Prisma Segitiga
volume = Label(frame, text="Volume Prisma Segitiga:")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Segitiga
txtLuas_Segitiga = Entry(frame)
txtLuas_Segitiga.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling Segitiga
txtKeliling_Segitiga = Entry(frame)
txtKeliling_Segitiga.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Prisma Segitiga
txtLuas_Permukaan_Prisma_Segitiga = Entry(frame)
txtLuas_Permukaan_Prisma_Segitiga.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume Prisma Segitiga
txtVolume_Prisma_Segitiga = Entry(frame)
txtVolume_Prisma_Segitiga.grid(row=8, column=1, sticky=W, padx=5, pady=5)

# Nama, NIM dan Kelas
nametag = Frame(frame, bg="lightblue", height=30)
nametag.grid(row=9, column=0, columnspan=3, sticky="ew", pady=10)

nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
nama.grid(row=9, column=0, sticky='e', padx=5, pady=5)

nim = Label(nametag, text="220511078", bg='lightblue')
nim.grid(row=9, column=2, sticky="e", padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue') 
kelas.grid(row=9, column=3, sticky='e', padx=5, pady=5)

app.mainloop()
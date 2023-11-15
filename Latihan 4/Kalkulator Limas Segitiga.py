import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
from FUNGSI import Volume_Limas_Segitiga, Luas_Segitiga, Keliling_Segitiga, Luas_Permukaan_Limas_Segitiga

def hitung():
    Luas_Segitiga(txtPanjang, txtTinggi_Segitiga_Dasar, txtLuas_Segitiga)
    Keliling_Segitiga(txtPanjang, txtKeliling_Segitiga)
    Luas_Permukaan_Limas_Segitiga(txtTinggi_Limas, txtLuas_Segitiga, txtKeliling_Segitiga, txtLuas_Permukaan_Limas_Segitiga)
    Volume_Limas_Segitiga(txtLuas_Segitiga, txtTinggi_Limas, txtVolume_Limas_Segitiga)
    

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Limas Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang Sisi Segitiga Dasar
Panjang = Label(frame, text="Panjang Sisi Segitiga Dasar:")
Panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Segitiga Dasar
TinggiSegitigaDasar = Label(frame, text="Tinggi Segitiga Dasar:")
TinggiSegitigaDasar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Limas
TinggiLimas = Label(frame, text="Tinggi Limas:")
TinggiLimas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi Tinggi Alas
TinggiAlas = Label(frame, text="Tinggi Segitiga Alas:")
TinggiAlas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#Textbox Panjang Sisi Segitiga Dasar
txtPanjang = Entry(frame)
txtPanjang.grid(row=0, column=1)

#Textbox Tinggi Segitiga Dasar
txtTinggi_Segitiga_Dasar = Entry(frame)
txtTinggi_Segitiga_Dasar.grid(row=1, column=1)

# Textbox Tinggi Limas
txtTinggi_Limas = Entry(frame)
txtTinggi_Limas.grid(row=2, column=1)

# Textbox Tinggi Alas
txtTinggi_Alas = Entry(frame)
txtTinggi_Alas.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Segitiga
LuasSegitiga = Label(frame, text="Luas Segitiga:")
LuasSegitiga.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Keliling Segitiga
KelilingSegitiga = Label(frame, text="Keliling Segitiga:")
KelilingSegitiga.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Segitiga
txtLuas_Segitiga = Entry(frame)
txtLuas_Segitiga.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling Segitiga
txtKeliling_Segitiga = Entry(frame)
txtKeliling_Segitiga.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Permukaan_Limas_Segitiga = Entry(frame)
txtLuas_Permukaan_Limas_Segitiga.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume_Limas_Segitiga = Entry(frame)
txtVolume_Limas_Segitiga.grid(row=8, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
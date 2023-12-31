import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W

def hitung_luas_segitiga():
    P = float(txtPanjang.get())
    TSD = float(txtTinggiSegitigaDasar.get())
    
    LS = 0.5 * P * TSD
    
    txtLuas_Segitiga.delete(0,END)
    txtLuas_Segitiga.insert(END,LS)
    
def hitung_keliling_segitiga():
    P = float(txtPanjang.get())
 
    KS = 3 * P
    
    txtKeliling_Segitiga.delete(0,END)
    txtKeliling_Segitiga.insert(END,KS)
    
def hitung_luas():
    TL = float(txtTinggiLimas.get())
    LS = float(txtLuas_Segitiga.get())
    KS = float(txtKeliling_Segitiga.get())

    LP = LS + (1/2) * KS * TL

    txtLuas_Permukaan.delete(0,END)
    txtLuas_Permukaan.insert(END,LP)

def hitung_volume():
    TL = float(txtTinggiLimas.get())
    LS = float(txtLuas_Segitiga.get())
    
    V = (1/3) * LS * TL

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas_segitiga()
    hitung_keliling_segitiga()
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Limas Segitiga")

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

#Textbox Panjang Sisi Segitiga Dasar
txtPanjang = Entry(frame)
txtPanjang.grid(row=0, column=1)

#Textbox Tinggi Segitiga Dasar
txtTinggiSegitigaDasar = Entry(frame)
txtTinggiSegitigaDasar.grid(row=1, column=1)

# Textbox Tinggi Limas
txtTinggiLimas = Entry(frame)
txtTinggiLimas.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Segitiga
LuasSegitiga = Label(frame, text="Luas Segitiga:")
LuasSegitiga.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Keliling Segitiga
KelilingSegitiga = Label(frame, text="Keliling Segitiga:")
KelilingSegitiga.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Limas Segitiga
luas = Label(frame, text="Luas Limas Segitiga:")
luas.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume Limas Segitiga
volume = Label(frame, text="Volume Limas Segitiga:")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Segitiga
txtLuas_Segitiga = Entry(frame)
txtLuas_Segitiga.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling Segitiga
txtKeliling_Segitiga = Entry(frame)
txtKeliling_Segitiga.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Limas Segitiga
txtLuas_Permukaan = Entry(frame)
txtLuas_Permukaan.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume Limas Segitiga
txtVolume = Entry(frame)
txtVolume.grid(row=8, column=1, sticky=W, padx=5, pady=5)

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
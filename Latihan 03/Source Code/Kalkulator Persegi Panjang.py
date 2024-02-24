import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W

def Hitung_Luas_Persegi_Panjang():
    Panjang = float(txtPanjang.get())
    Lebar = float(txtLebar.get())

    Luas = Panjang * Lebar 

    txtLuas_Persegi_Panjang.delete(0,END)
    txtLuas_Persegi_Panjang.insert(END,Luas)

def Hitung_Keliling_Persegi_Panjang():
    Panjang = float(txtPanjang.get())
    Lebar = float(txtLebar.get())

    Keliling = (2 * Panjang) + (2 * Lebar)

    txtKeliling_Persegi_Panjang.delete(0,END)
    txtKeliling_Persegi_Panjang.insert(END,Keliling)

def Hitung():
    Hitung_Luas_Persegi_Panjang()
    Hitung_Keliling_Persegi_Panjang()

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Keliling Persegi Panjang")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang
Panjang = Label(frame, text="Panjang:")
Panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Lebar
Lebar = Label(frame, text="Lebar:")
Lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtPanjang = Entry(frame)
txtPanjang.grid(row=0, column=1)

# Textbox Lebar
txtLebar = Entry(frame)
txtLebar.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Persegi Panjang
Luas_Persegi_Panjang = Label(frame, text="Luas Persegi Panjang:")
Luas_Persegi_Panjang.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Keliling Persegi Panjang
Keliling_Persegi_Panjang = Label(frame, text="Keliling Persegi Panjang:")
Keliling_Persegi_Panjang.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Persegi Panjang
txtLuas_Persegi_Panjang = Entry(frame)
txtLuas_Persegi_Panjang.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling Persegi Panjang
txtKeliling_Persegi_Panjang = Entry(frame)
txtKeliling_Persegi_Panjang.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Nama, NIM dan Kelas
nametag = Frame(frame, bg="lightblue", height=30)
nametag.grid(row=5, column=0, columnspan=3, sticky="ew", pady=10)

nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
nama.grid(row=5, column=0, sticky='e', padx=5, pady=5)

nim = Label(nametag, text="220511078", bg='lightblue')
nim.grid(row=5, column=2, sticky="e", padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue') 
kelas.grid(row=5, column=3, sticky='e', padx=5, pady=5)

app.mainloop()
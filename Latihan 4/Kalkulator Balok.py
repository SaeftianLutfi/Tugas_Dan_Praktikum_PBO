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

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Balok = Entry(frame)
txtLuas_Balok.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume_Balok = Entry(frame)
txtVolume_Balok.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
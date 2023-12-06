import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
from FUNGSI import Luas_Kubus, Volume_Kubus

def Hitung():
    Luas_Kubus(txtSisi, txtLuas_Kubus)
    Volume_Kubus(txtSisi, txtVolume_Kubus)
    
# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Kubus")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Sisi
Sisi = Label(frame, text="Sisi:")
Sisi.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Textbox Sisi
txtSisi = Entry(frame)
txtSisi.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Kubus
luas = Label(frame, text="Luas Kubus:")
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume Kubus
volume = Label(frame, text="Volume Kubus:")
volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Kubus
txtLuas_Kubus = Entry(frame)
txtLuas_Kubus.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume Kubus
txtVolume_Kubus = Entry(frame)
txtVolume_Kubus.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Nama, NIM dan Kelas
nametag = Frame(frame, bg="lightblue", height=30)
nametag.grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
nama.grid(row=4, column=0, sticky='e', padx=5, pady=5)

nim = Label(nametag, text="220511078", bg='lightblue')
nim.grid(row=4, column=2, sticky="e", padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue') 
kelas.grid(row=4, column=3, sticky='e', padx=5, pady=5)

app.mainloop()
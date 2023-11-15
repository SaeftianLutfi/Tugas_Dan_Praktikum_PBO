import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
from FUNGSI import Luas_Kubus, Volume_Kubus

def Hitung():
    Luas_Kubus(txtSisi, txtLuas_Kubus)
    Volume_Kubus(txtSisi, txtVolume_Kubus)
    
# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Alas dan Volume Kubus")

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

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan:")
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Kubus = Entry(frame)
txtLuas_Kubus.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume_Kubus = Entry(frame)
txtVolume_Kubus.grid(row=3, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
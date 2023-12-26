import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

# Rumus
def get_celcius():
    suhu = txtsuhu.get()
    C = float(suhu) - 273
    txtCelcius.delete(0, END)
    txtCelcius.insert(END, str(C))
    
def get_fahrenheit():
    suhu = txtsuhu.get()
    F = 9/5 * (float(suhu) - 273) + 32
    txtFahrenheit.delete(0, END)
    txtFahrenheit.insert(END, str(F))
    
def get_reamur():
    suhu = txtsuhu.get()
    R = 4/5 * (float(suhu) - 273)
    txtReamur.delete(0, END)
    txtReamur.insert(END, str(R))
    
def Hitung():
    get_celcius()
    get_fahrenheit()
    get_reamur()
    
# create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Program Menghitung Suhu Kelvin")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label
suhu = Label(frame, text="Kelvin:")
suhu.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox
txtsuhu = Entry(frame)
txtsuhu.grid(row=0, column=1, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=Hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Output Label
C = Label(frame, text="Celcius:")
C.grid(row=2, column=0, sticky=W, padx=5, pady=5)

F = Label(frame, text="Fahrenheit:")
F.grid(row=3, column=0, sticky=W, padx=5, pady=5)

R = Label(frame, text="Reamur:")
R.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox
txtCelcius = Entry(frame)
txtCelcius.grid(row=2, column=1, sticky=W, padx=5, pady=5)

txtFahrenheit = Entry(frame)
txtFahrenheit.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtReamur = Entry(frame)
txtReamur.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Nama, NIM dan Kelas
nametag = Frame(frame, bg="lightgreen", height=30)
nametag.grid(row=5, column=0, columnspan=3, sticky="ew", pady=10)

nama = Label(nametag, text="Saeftian Lutfi", bg='lightgreen') 
nama.grid(row=5, column=0, sticky='e', padx=5, pady=5)

nim = Label(nametag, text="220511078", bg='lightgreen')
nim.grid(row=5, column=2, sticky="e", padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightgreen')
kelas.grid(row=5, column=3, sticky='e', padx=5, pady=5)

app.mainloop()
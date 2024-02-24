import tkinter as tk
from tkinter import Menu, ttk
from FrmPersegiPanjang import *
from FrmBalok import *
from FrmBola import *
from FrmKerucut import *
from FrmKubus import *
from FrmLimasSegiempat import *
from FrmLimasSegitiga import *
from FrmPersegiPanjang import *
from FrmPrismaSegitiga import *
from FrmTabung import *
    
# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Kalkulator Persegi Panjang', command= lambda: new_window("Persegi Panjang", FrmPersegiPanjang)
)
app_menu.add_command(
    label='App Kalkulator Balok', command= lambda: new_window("Balok", FrmBalok)
)
app_menu.add_command(
    label='App Kalkulator Bola', command= lambda: new_window("Bola", FrmBola)
)
app_menu.add_command(
    label='App Kalkulator Kerucut', command= lambda: new_window("Kerucut", FrmKerucut)
)
app_menu.add_command(
    label='App Kalkulator Kubus', command= lambda: new_window("Kubus", FrmKubus)
)
app_menu.add_command(
    label='App Kalkulator Limas Segiempat', command= lambda: new_window("Limas Segiempat", FrmLimasSegiempat)
)
app_menu.add_command(
    label='App Kalkulator Limas Segitiga', command= lambda: new_window("Limas Segitiga", FrmLimasSegitiga)
)
app_menu.add_command(
    label='App Kalkulator Prisma Segitiga', command= lambda: new_window("Prisma Segitiga", FrmPrismaSegitiga)
)
app_menu.add_command(
    label='App Kalkulator Tabung', command= lambda: new_window("Tabung", FrmTabung)
)

def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)

# Nama, NIM dan Kelas
frame = Frame(root) 
frame.pack(padx=5, pady=5)

nametag = Frame(frame, bg="lightblue", height=30)
nametag.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
nama.grid(row=1, column=0, sticky='e', padx=5, pady=5)
        
nim = Label(nametag, text="220511078", bg='lightblue')
nim.grid(row=1, column=1, sticky='e', padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue') 
kelas.grid(row=1, column=2, sticky='e', padx=5, pady=5)
        
root.mainloop()
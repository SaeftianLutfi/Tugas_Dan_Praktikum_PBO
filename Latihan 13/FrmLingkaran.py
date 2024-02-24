from tkinter import *
import math

class Frmlingkaran:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry("200x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainFrame, text="Jari-jari: ").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas: ").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        
        # Pasang TextBox
        self.txtJarijari = Entry(mainFrame)
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=2, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.txtbtnHitung = Button(mainFrame, text="Hitung", command=self.onHitung)
        self.txtbtnHitung.grid(row=1, column=1, padx=5, pady=5)
        
    # Fungsi "onHitung" untuk menghitung luas lingkaran
    def onHitung(self, event=None):
        r = int(self.txtJarijari.get())
        Luas = math.pi * r ** 2
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(Luas))
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
    root = Tk()
    aplikasi = Frmlingkaran(root, "Aplikasi Menghitung Luas Lingkaran")
    root.mainloop()    
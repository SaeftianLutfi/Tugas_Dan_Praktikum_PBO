from tkinter import *

class Frmpersegipanjang:
    def __init__(self, parent, title, update_new_window):
        self.parent = parent
        self.update_new_window = update_new_window
        #self.parent.geomaetry('200x200')
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainFrame, text="Pannjang: ").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Lebar: ").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas: ").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        
        # Pasang TextBox
        self.txtPanjang = Entry(mainFrame)
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtLebar = Entry(mainFrame)
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text="Hitung", command = self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
    def onHitung(self, event=None):
        Panjang = int(self.txtPanjang.get())
        Lebar = int(self.txtLebar.get())
        Luas = Panjang * Lebar
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(Luas))
        
    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
    root = Tk()
    aplikasi = Frmpersegipanjang(root, "Program Luas Persegi Panjang")
    root.mainloop()
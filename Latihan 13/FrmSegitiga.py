from tkinter import *

class Frmsegitiga:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry("300x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainFrame, text="Lebar Alas: ").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi: ").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Segitiga: ").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        
        # Pasang TextBox
        self.txtAlas = Entry(mainFrame)
        self.txtAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi =  Entry(mainFrame)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.txtbtnHitung = Button(mainFrame, text="Hitung", command=self.onHitung)
        self.txtbtnHitung.grid(row=2, column=1, padx=5, pady=5)
        
    def onHitung(self, event=None):
        Alas = int(self.txtAlas.get())
        Tinggi = int(self.txtTinggi.get())
        Luas =  0.5 * Alas * Tinggi
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(Luas))
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
    root = Tk()
    aplikasi = Frmsegitiga(root, "Program Luas Segitiga")
    root.mainloop()
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import math

class FrmBola:
    def __init__(self, parent, title):
        self.parent = parent
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainFrame, text="Jari-jari:").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Luas Bola:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Volume Bola:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        
        # Nama, NIM dan Kelas
        nametag = Frame(mainFrame, bg="lightblue", height=30)
        nametag.grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

        nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
        nama.grid(row=4, column=0, sticky='e', padx=5, pady=5)

        nim = Label(nametag, text="220511078", bg='lightblue')
        nim.grid(row=4, column=2, sticky="e", padx=5, pady=5)

        kelas = Label(nametag, text="TIF22E", bg='lightblue') 
        kelas.grid(row=4, column=3, sticky='e', padx=5, pady=5)
        
        # Pasang TextBox
        self.txtJarijari = Entry(mainFrame)
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=2, column=1, padx=5, pady=5)
        
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=3, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command = self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)
        
    # Fungsi "onHitung" berfungsi untuk menghitung Luas dan Volume Bola
    def onHitung(self, event=None):
        r = int(self.txtJarijari.get())
        
        Luas = 4 * math.pi * r ** 2
        Volume = (4/3) * math.pi * r ** 3
        
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, (Luas))
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, (Volume))
        
    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmBola(root, "Program Kalkulator Bola")
    root.mainloop()
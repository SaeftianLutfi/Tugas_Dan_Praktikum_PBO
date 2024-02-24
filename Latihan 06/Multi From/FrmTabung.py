from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import math

class FrmTabung:
    def __init__(self, parent, title):
        self.parent = parent
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainframe = Frame(self.parent, bd=10)
        mainframe.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainframe, text='Jari-Jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Tinggi:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Luas Tabung:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Volume Tabung:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        # Nama, NIM dan Kelas
        nametag = Frame(mainframe, bg="lightblue", height=30)
        nametag.grid(row=5, column=0, columnspan=3, sticky="ew", pady=10)

        nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
        nama.grid(row=5, column=0, sticky='e', padx=5, pady=5)

        nim = Label(nametag, text="220511078", bg='lightblue')
        nim.grid(row=5, column=2, sticky="e", padx=5, pady=5)

        kelas = Label(nametag, text="TIF22E", bg='lightblue') 
        kelas.grid(row=5, column=3, sticky='e', padx=5, pady=5)

        
        # Pasang TextBox
        self.txtJarijari = Entry(mainframe)
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtTinggi = Entry(mainframe)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        
        self.txtLuasTabung = Entry(mainframe)
        self.txtLuasTabung.grid(row=3, column=1, padx=5, pady=5)
        
        self.txtVolumeTabung = Entry(mainframe)
        self.txtVolumeTabung.grid(row=4, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainframe, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
        # Fungsi "onHitung" berfungsi untuk menghitung Luas dan Volume Limas Segitiga
    def onHitung(self, event=None):
        r = int(self.txtJarijari.get())
        T = int(self.txtTinggi.get())
                
        Luas = 2 * math.pi * r * (r + T)
        Volume = math.pi * r ** 2 * T
        
        self.txtLuasTabung.delete(0, END)
        self.txtLuasTabung.insert(END, (Luas))
        self.txtVolumeTabung.delete(0, END)
        self.txtVolumeTabung.insert(END, (Volume))
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmTabung(root, "Program Kalkulator Tabung")
    root.mainloop()
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmLimasSegitiga:
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
        Label(mainframe, text='Panjang:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Tinggi Segitiga Dasar:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Tinggi Limas:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Keliling Segitiga:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Luas Segitiga:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Luas Limas Segitiga:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Volume Limas Segitiga:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        
        # Nama, NIM dan Kelas
        nametag = Frame(mainframe, bg="lightblue", height=30)
        nametag.grid(row=9, column=0, columnspan=3, sticky="ew", pady=10)

        nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
        nama.grid(row=9, column=0, sticky='e', padx=5, pady=5)

        nim = Label(nametag, text="220511078", bg='lightblue')
        nim.grid(row=9, column=2, sticky="e", padx=5, pady=5)

        kelas = Label(nametag, text="TIF22E", bg='lightblue') 
        kelas.grid(row=9, column=3, sticky='e', padx=5, pady=5)

        
        # Pasang TextBox
        self.txtPanjang = Entry(mainframe)
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtTinggiSegitigaDasar = Entry(mainframe)
        self.txtTinggiSegitigaDasar.grid(row=1, column=1, padx=5, pady=5)
        
        self.txtTinggiLimas = Entry(mainframe)
        self.txtTinggiLimas.grid(row=2, column=1, padx=5, pady=5)
        
        self.txtKelilingSegitiga = Entry(mainframe)
        self.txtKelilingSegitiga.grid(row=4, column=1, padx=5, pady=5)
        
        self.txtLuasSegitiga = Entry(mainframe)
        self.txtLuasSegitiga.grid(row=5, column=1, padx=5, pady=5)
        
        self.txtLuasLimasSegitiga = Entry(mainframe)
        self.txtLuasLimasSegitiga.grid(row=6, column=1, padx=5, pady=5)
        
        self.txtVolumeLimasSegitiga = Entry(mainframe)
        self.txtVolumeLimasSegitiga.grid(row=7, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainframe, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
        # Fungsi "onHitung" berfungsi untuk menghitung Luas dan Volume Limas Segitiga
    def onHitung(self, event=None):
        P = int(self.txtPanjang.get())
        TSD = int(self.txtTinggiSegitigaDasar.get())
        TL = int(self.txtTinggiLimas.get())
        
        LS = 0.5 * P * TSD
        KS = 3 * P
        Luas = LS + (1/2) * KS * TL
        Volume = (1/3) * LS * TL
        
        self.txtLuasSegitiga.delete(0, END)
        self.txtLuasSegitiga.insert(END, (LS))
        self.txtKelilingSegitiga.delete(0, END)
        self.txtKelilingSegitiga.insert(END, (KS))
        self.txtLuasLimasSegitiga.delete(0, END)
        self.txtLuasLimasSegitiga.insert(END, (Luas))
        self.txtVolumeLimasSegitiga.delete(0, END)
        self.txtVolumeLimasSegitiga.insert(END, (Volume))
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLimasSegitiga(root, "Program Kalkulator Limas Segitiga")
    root.mainloop()
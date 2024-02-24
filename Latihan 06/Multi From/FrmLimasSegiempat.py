from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,W,Tk

class FrmLimasSegiempat:
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
        Label(mainframe, text='Lebar:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Tinggi Alas:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Tinggi:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Luas Limas Segiempat:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainframe, text='Volume Limas Segiempat:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        
        # Nama, NIM dan Kelas
        nametag = Frame(mainframe, bg="lightblue", height=30)
        nametag.grid(row=7, column=0, columnspan=3, sticky="ew", pady=10)

        nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
        nama.grid(row=7, column=0, sticky='e', padx=5, pady=5)

        nim = Label(nametag, text="220511078", bg='lightblue')
        nim.grid(row=7, column=2, sticky="e", padx=5, pady=5)

        kelas = Label(nametag, text="TIF22E", bg='lightblue') 
        kelas.grid(row=7, column=3, sticky='e', padx=5, pady=5)

        
        # Pasang TextBox
        self.txtPanjang = Entry(mainframe)
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtLebar = Entry(mainframe)
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)
        
        self.txtTinggiAlas = Entry(mainframe)
        self.txtTinggiAlas.grid(row=2, column=1, padx=5, pady=5)
        
        self.txtTinggi = Entry(mainframe)
        self.txtTinggi.grid(row=3, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(mainframe)
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5)
        
        self.txtVolume = Entry(mainframe)
        self.txtVolume.grid(row=6, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainframe, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=4, column=1, padx=5, pady=5)
        
    # Fungsi "onHitung" berfungasi untuk menghitung Luas dan Volume Limas Segiempat
    def onHitung(self, event=None):
        P = int(self.txtPanjang.get())
        Lb = int(self.txtLebar.get())
        TA = int(self.txtTinggiAlas.get())
        T = int(self.txtTinggi.get())
        
        Luas = P * Lb + 2 * P * TA + 2 * Lb * TA
        Volume = (1/3) * P * Lb * T
        
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END, (Luas))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END, (Volume))
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLimasSegiempat(root, "Program Kalkulator Limas Segiempat")
    root.mainloop()
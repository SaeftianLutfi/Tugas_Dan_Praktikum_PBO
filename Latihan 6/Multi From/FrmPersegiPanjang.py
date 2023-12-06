from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmPersegiPanjang:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Panjang:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Lebar:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Keliling:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text='Luas:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        # Nama, NIM dan Kelas
        nametag = Frame(mainFrame, bg="lightblue", height=30)
        nametag.grid(row=5, column=0, columnspan=3, sticky="ew", pady=10)

        nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
        nama.grid(row=5, column=0, sticky='e', padx=5, pady=5)

        nim = Label(nametag, text="220511078", bg='lightblue')
        nim.grid(row=5, column=2, sticky="e", padx=5, pady=5)

        kelas = Label(nametag, text="TIF22E", bg='lightblue') 
        kelas.grid(row=5, column=3, sticky='e', padx=5, pady=5)


        # pasang textbox
        self.txtPanjang = Entry(mainFrame) 
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)  
        
        self.txtLebar = Entry(mainFrame) 
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5) 
        
        self.txtKeliling = Entry(mainFrame) 
        self.txtKeliling.grid(row=3, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung Keliling dan Luas Persegi Panjang 
    def onHitung(self, event=None):
        Panjang = int(self.txtPanjang.get())
        Lebar = int(self.txtLebar.get())
        Keliling = (2 * Panjang) + (2 * Lebar)
        Luas = Panjang * Lebar
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END,str(Keliling))
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END, str(Luas))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPersegiPanjang(root, "Program Kalkulator Persegi Panjang")
    root.mainloop() 
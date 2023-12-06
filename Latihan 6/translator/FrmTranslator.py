from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from tkinter import ttk
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("650x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Bahasa: ').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Bahasa: ').grid(row=0, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Masukkan teks:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:').grid(row=2, column=1,
            sticky=W, padx=5, pady=5)
        
        # Nama, NIM dan Kelas
        frame = Frame(root) 
        frame.pack(padx=5, pady=5)

        nametag = Frame(frame, bg="lightblue", height=30)
        nametag.grid(row=5, column=0, columnspan=2, sticky="ew", pady=10)

        nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
        nama.grid(row=5, column=0, sticky='e', padx=5, pady=5)
        
        nim = Label(nametag, text="220511078", bg='lightblue')
        nim.grid(row=5, column=1, sticky='e', padx=5, pady=5)

        kelas = Label(nametag, text="TIF22E", bg='lightblue') 
        kelas.grid(row=5, column=2, sticky='e', padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=3, column=0, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=3, column=1, padx=5, pady=5)

        # Pasang Combobox 1
        self.Dari_Bahasa_Combobox = ttk.Combobox(mainFrame, values=["id", "en", "ja", "tl", "ar"])
        self.Dari_Bahasa_Combobox.grid(row=1, column=0, padx=5, pady=5)
        self.Dari_Bahasa_Combobox.set("id")
        
        # Pasang Combobox 2
        self.Trans_Bahasa_Combobox = ttk.Combobox(mainFrame, values=["id", "en", "ja", "tl", "ar"])
        self.Trans_Bahasa_Combobox.grid(row=1, column=1, padx=5, pady=5)
        self.Trans_Bahasa_Combobox.set("en")
        
        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!', width=20,
            command=self.onTranslate)
        self.btnTranslate.grid(row=4, column=0, columnspan=2, padx=5, pady=5) 

    def onTranslate(self):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        Hasil = penterjemah.translate(
            self.txtSumber.get(),
            src=self.Dari_Bahasa_Combobox.get(),
            dest=self.Trans_Bahasa_Combobox.get()
        )
        
        # Menampilkan Hasil Terjemah Bahasa
        self.txtHasil.delete(0, END)
        self.txtHasil.insert(END, Hasil.text)
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop() 
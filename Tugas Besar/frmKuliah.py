import tkinter as tk
from tkinter import Frame, Label, ttk, messagebox, Entry, Button, YES, BOTH, END, Tk, W
from MataKuliah import *

class FrmKuliah1:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry('300x200')
        self.parent.title(title)
        self.ditemukan = None
        self.parent.protocol("WM_DELETE_WINDOW", self.onCancel)
        self.aturKomponen()
        self.onReload
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 100) // 2
        y = (screen_height - 100) // 2
        width = 800
        height = 500
        self.parent.geometry(f"{width}x{height}+{x}+{y}")
        
        # Label & Entry
        Label(mainFrame, text='ID').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtID = Entry(mainFrame)
        self.txtID.grid(row=0, column=1, padx=5, pady=5)
        self.txtID.bind("<Return>", self.onCari)
        
        Label(mainFrame, text='Semester').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtSemester = tk.StringVar()
        self.CboMain = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtSemester)
        self.CboMain.grid(row=1, column=1,padx=5, pady=5)
        self.CboMain['values'] = ('Semester 1', 'Semester 2', 'Semester 3', 'Semester 4','Semester 5', 'Semester 6', 'Semester 7', 'Semester 8')
        self.CboMain.bind("<<ComboboxSelected>>", self.update_subcategories)
        self.CboMain.current()

        Label(mainFrame, text='Mata Kuliah').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtMk = tk.StringVar()
        self.CboSub1 = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtMk)
        self.CboSub1.grid(row=2, column=1,padx=5, pady=5)
        self.CboSub1.current()

        Label(mainFrame, text='SKS').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = Entry(mainFrame)
        self.txtSKS.grid(row=3, column=1, padx=5, pady=5)
        
        Label(mainFrame, text='Kelas').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtKelas = tk.StringVar()
        self.Cbokelas = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtKelas)
        self.Cbokelas.grid(row=4, column=1,padx=5, pady=5)
        self.Cbokelas['values'] = ('Kelas A', 'Kelas B', 'Kelas C', 'Kelas D', 'Kelas E', 'Kelas K', 'Kelas L')
        self.Cbokelas.current()

        # Button
        self.btnSubmit = Button(mainFrame, text='Submit', command=self.onSubmit)
        self.btnSubmit.grid(row=0, column=2, padx=5, pady=5)
        self.btnDelete = Button(mainFrame, text='Delete', command=self.onDelete)
        self.btnDelete.grid(row=1, column=2, padx=5,pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear)
        self.btnClear.grid(row=2, column=2, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onCancel)
        self.btnCancel.grid(row=3, column=2, padx=5, pady=5)
        
        # Tabel
        column = ("ID", "Semester","Mata_Kuliah", "SKS", "Kelas")
        self.tree = ttk.Treeview(mainFrame, columns=column, show='headings')
        
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width='30')
        self.tree.heading('Semester', text='Semester')
        self.tree.column('Semester', width='100')
        self.tree.heading('Mata_Kuliah', text='Mata Kuliah')
        self.tree.column('Mata_Kuliah', width='150')
        self.tree.heading('SKS', text='SKS')
        self.tree.column('SKS', width='75')
        self.tree.heading('Kelas', text='Kelas')
        self.tree.column('Kelas', width='100')
        
        # Set Position
        self.tree.place(x=0, y=200)
        self.onReload()

    def update_subcategories(self, event):
        select_subcategories = self.CboMain.get()

        self.CboSub1.set('')
        self.CboSub1['values'] = []

        if select_subcategories == 'Semester 1':
            subcategories = ['Agama', 'Matematika', 'Fisika','Bahasa Inggris','Pancasila', 'Logika Matematika', 'Dasar Algoritma dan Pemrograman', 'Praktik Dasar Algoritma dan Pemrograman', 'Pengantar Teknologi Informasi']
        elif select_subcategories == 'Semester 2':
            subcategories = ['Sistem Operasi', 'Kalkulus 1', 'Kewirausahaan Islami', 'AIK 1 (Kemanusiaan dan Keimanan)', 'Bahasa Indonesia','Kewarganegaraan','Pemrograman Terstruktur','Sistem Digital']
        elif select_subcategories == 'Semester 3':
            subcategories = ['Struktur Data dan Algoritma', 'Komunikasi Data', 'Pemrograman II (PBO)', 'Statistik dan Probabilitas', 'Arsitektur dan Organisasi Komputer', 'Sistem Informasi', 'AIK 2', 'Kalkulus 2']
        elif select_subcategories == 'Semester 4':
            subcategories = ['AIK 3','Kewirausahaan Berbasis Teknologi','Pemrograman Fungsional','Jaringan Komputer','Rekayasa Perangkat Lunak', 'Teori Bahasa Otomata', 'Pemrograman Web']
        elif select_subcategories == 'Semester 5':
            subcategories = ['Basis Data','Pemrograman Mobile','AIK 4','Metode Penelitian','Keamanan dan Keselamatan Kerja','Pemrograman Jaringan','Pemrograman Paralel']
        elif select_subcategories == 'Semester 6':
            subcategories = ['Pre Skripsi','Etika dan Profesi','Manajemen Proyek Perangkat Lunak','Rekayasa Ulang Sistem','Manajemen Jaringan','Keamanan Jaringan','Analisis Big Data']
        elif select_subcategories == 'Semester 7':
            subcategories = ['Permodelan dan Simulasi Data','Penalaran Komputer','Pemrograman Game','Desain Perangkat Lunak','Penulisan Desain Game']
        elif select_subcategories == 'Semester 8':
            subcategories = ['Kuliah Kerja Nyata','Praktek Kerja Nyata','Skripsi']
        
        self.CboSub1['values'] = subcategories
        
    def onCari(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah1()
        res = kul1.getByID(id)
        rec = kul1.affected
        if (rec>0) :
            messagebox.showinfo("Berhasil!", "Data Ditemukan")
            self.tampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Warning!", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtSKS.focus()
        return res
            
    def tampilkanData(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah1()
        res = kul1.getByID(id)
        self.txtSemester.set(kul1.semester)
        self.txtMk.set(kul1.matakuliah)
        self.txtSKS.delete(0, END)
        self.txtSKS.insert(END,kul1.sks)
        self.txtKelas.set(kul1.kelas)
        self.btnSubmit.config(text='Update')
        
    def onSubmit(self):
        id = self.txtID.get()
        semester = self.txtSemester.get()
        mata_kuliah = self.txtMk.get()
        sks = self.txtSKS.get()
        kelas = self.txtKelas.get()

        kul1 = Kuliah1()
        kul1.id = id
        kul1.semester = semester
        kul1.matakuliah = mata_kuliah
        kul1.sks = sks
        kul1.kelas = kelas
        if(self.ditemukan == True):
            res = kul1.update(id)
            ket = 'Diperbarui'
        else:
            res = kul1.simpan()
            ket = 'Disimpan'
            
        rec =kul1.affected
        if(rec>0):
            messagebox.showinfo("Information", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("Warning!", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onClear(self):
        self.txtID.delete(0,END)
        self.txtID.insert(END, "")
        self.txtSemester.set("")
        self.txtMk.set("")
        self.txtSKS.delete(0,END)
        self.txtSKS.insert(END,"")
        self.txtKelas.set("")
        self.btnClear.config(text='Clear')
        self.onReload()
        self.ditemukan = False

    def onDelete(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah1()
        kul1.id = id
        if(self.ditemukan==True):
            res = kul1.delete(id)
            rec = kul1.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
        
    def onReload(self):
        kul1 = Kuliah1()
        result = kul1.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        kuliah = []
        for row_data in result:
            kuliah.append(row_data)
        
        for kuliah in kuliah:
            self.tree.insert('', END, values=kuliah)
        
    def onCancel(self, event=None):
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
        root = tk.Tk()
        aplikasi = FrmKuliah1(root, "Data Mata Kuliah Mahasiswa", update_main_window)
        root.mainloop()


# Frm Kuliah 2
class FrmKuliah2:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry('300x200')
        self.parent.title(title)
        self.ditemukan = None
        self.parent.protocol("WM_DELETE_WINDOW", self.onCancel)
        self.aturKomponen()
        self.onReload
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 100) // 2
        y = (screen_height - 100) // 2
        width = 800
        height = 500
        self.parent.geometry(f"{width}x{height}+{x}+{y}")
        
        # Label & Entry
        Label(mainFrame, text='ID').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtID = Entry(mainFrame)
        self.txtID.grid(row=0, column=1, padx=5, pady=5)
        self.txtID.bind("<Return>", self.onCari)
        
        Label(mainFrame, text='Semester').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtSemester = tk.StringVar()
        self.CboMain = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtSemester)
        self.CboMain.grid(row=1, column=1,padx=5, pady=5)
        self.CboMain['values'] = ('Semester 1', 'Semester 2', 'Semester 3', 'Semester 4','Semester 5', 'Semester 6', 'Semester 7', 'Semester 8')
        self.CboMain.bind("<<ComboboxSelected>>", self.update_subcategories)
        self.CboMain.current()

        Label(mainFrame, text='Mata Kuliah').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtMk = tk.StringVar()
        self.CboSub1 = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtMk)
        self.CboSub1.grid(row=2, column=1,padx=5, pady=5)
        self.CboSub1.current()

        Label(mainFrame, text='SKS').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = Entry(mainFrame)
        self.txtSKS.grid(row=3, column=1, padx=5, pady=5)
        
        Label(mainFrame, text='Kelas').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtKelas = tk.StringVar()
        self.Cbokelas = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtKelas)
        self.Cbokelas.grid(row=4, column=1,padx=5, pady=5)
        self.Cbokelas['values'] = ('Kelas A', 'Kelas B', 'Kelas C', 'Kelas D', 'Kelas E', 'Kelas K', 'Kelas L')
        self.Cbokelas.current()

        # Button
        self.btnSubmit = Button(mainFrame, text='Submit', command=self.onSubmit)
        self.btnSubmit.grid(row=0, column=2, padx=5, pady=5)
        self.btnDelete = Button(mainFrame, text='Delete', command=self.onDelete)
        self.btnDelete.grid(row=1, column=2, padx=5,pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear)
        self.btnClear.grid(row=2, column=2, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onCancel)
        self.btnCancel.grid(row=3, column=2, padx=5, pady=5)
        
        # Tabel
        column = ("ID", "Semester","Mata_Kuliah", "SKS", "Kelas")
        self.tree = ttk.Treeview(mainFrame, columns=column, show='headings')
        
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width='30')
        self.tree.heading('Semester', text='Semester')
        self.tree.column('Semester', width='100')
        self.tree.heading('Mata_Kuliah', text='Mata Kuliah')
        self.tree.column('Mata_Kuliah', width='150')
        self.tree.heading('SKS', text='SKS')
        self.tree.column('SKS', width='75')
        self.tree.heading('Kelas', text='Kelas')
        self.tree.column('Kelas', width='100')
        
        # Set Position
        self.tree.place(x=0, y=200)
        self.onReload()

    def update_subcategories(self, event):
        select_subcategories = self.CboMain.get()

        self.CboSub1.set('')
        self.CboSub1['values'] = []

        if select_subcategories == 'Semester 1':
            subcategories = ['Agama', 'Matematika', 'Fisika','Bahasa Inggris','Pancasila', 'Logika Matematika', 'Dasar Algoritma dan Pemrograman', 'Praktik Dasar Algoritma dan Pemrograman', 'Pengantar Teknologi Informasi']
        elif select_subcategories == 'Semester 2':
            subcategories = ['Sistem Operasi', 'Kalkulus 1', 'Kewirausahaan Islami', 'AIK 1 (Kemanusiaan dan Keimanan)', 'Bahasa Indonesia','Kewarganegaraan','Pemrograman Terstruktur','Sistem Digital']
        elif select_subcategories == 'Semester 3':
            subcategories = ['Struktur Data dan Algoritma', 'Komunikasi Data', 'Pemrograman II (PBO)', 'Statistik dan Probabilitas', 'Arsitektur dan Organisasi Komputer', 'Sistem Informasi', 'AIK 2', 'Kalkulus 2']
        elif select_subcategories == 'Semester 4':
            subcategories = ['AIK 3','Kewirausahaan Berbasis Teknologi','Pemrograman Fungsional','Jaringan Komputer','Rekayasa Perangkat Lunak', 'Teori Bahasa Otomata', 'Pemrograman Web']
        elif select_subcategories == 'Semester 5':
            subcategories = ['Basis Data','Pemrograman Mobile','AIK 4','Metode Penelitian','Keamanan dan Keselamatan Kerja','Pemrograman Jaringan','Pemrograman Paralel']
        elif select_subcategories == 'Semester 6':
            subcategories = ['Pre Skripsi','Etika dan Profesi','Manajemen Proyek Perangkat Lunak','Rekayasa Ulang Sistem','Manajemen Jaringan','Keamanan Jaringan','Analisis Big Data']
        elif select_subcategories == 'Semester 7':
            subcategories = ['Permodelan dan Simulasi Data','Penalaran Komputer','Pemrograman Game','Desain Perangkat Lunak','Penulisan Desain Game']
        elif select_subcategories == 'Semester 8':
            subcategories = ['Kuliah Kerja Nyata','Praktek Kerja Nyata','Skripsi']
        
        self.CboSub1['values'] = subcategories
        
    def onCari(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah2()
        res = kul1.getByID(id)
        rec = kul1.affected
        if (rec>0) :
            messagebox.showinfo("Berhasil!", "Data Ditemukan")
            self.tampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Warning!", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtSKS.focus()
        return res
            
    def tampilkanData(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah2()
        res = kul1.getByID(id)
        self.txtSemester.set(kul1.semester)
        self.txtMk.set(kul1.matakuliah)
        self.txtSKS.delete(0, END)
        self.txtSKS.insert(END,kul1.sks)
        self.txtKelas.set(kul1.kelas)
        self.btnSubmit.config(text='Update')
        
    def onSubmit(self):
        id = self.txtID.get()
        semester = self.txtSemester.get()
        mata_kuliah = self.txtMk.get()
        sks = self.txtSKS.get()
        kelas = self.txtKelas.get()

        kul1 = Kuliah2()
        kul1.id = id
        kul1.semester = semester
        kul1.matakuliah = mata_kuliah
        kul1.sks = sks
        kul1.kelas = kelas
        if(self.ditemukan == True):
            res = kul1.update(id)
            ket = 'Diperbarui'
        else:
            res = kul1.simpan()
            ket = 'Disimpan'
            
        rec =kul1.affected
        if(rec>0):
            messagebox.showinfo("Information", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("Warning!", "Data Gagal "+ket)
        self.onClear()
        return rec
    
    def onDelete(self, event=None):
        id = self.txtID.get()
        kul2 = Kuliah2()
        kul2.id = id
        if(self.ditemukan==True):
            res = kul2.delete(id)
            rec = kul2.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()

    def onClear(self):
        self.txtID.delete(0,END)
        self.txtID.insert(END, "")
        self.txtSemester.set("")
        self.txtMk.set("")
        self.txtSKS.delete(0,END)
        self.txtSKS.insert(END,"")
        self.txtKelas.set("")
        self.btnClear.config(text='Clear')
        self.onReload()
        self.ditemukan = False
        
    def onReload(self):
        kul1 = Kuliah2()
        result = kul1.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        kuliah = []
        for row_data in result:
            kuliah.append(row_data)
        
        for kuliah in kuliah:
            self.tree.insert('', END, values=kuliah)
        
    def onCancel(self, event=None):
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
        root = tk.Tk()
        aplikasi = FrmKuliah2(root, "Data Mata Kuliah Mahasiswa", update_main_window)
        root.mainloop()


#Frm Kuliah 3
class FrmKuliah3:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry('300x200')
        self.parent.title(title)
        self.ditemukan = None
        self.parent.protocol("WM_DELETE_WINDOW", self.onCancel)
        self.aturKomponen()
        self.onReload
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 100) // 2
        y = (screen_height - 100) // 2
        width = 800
        height = 500
        self.parent.geometry(f"{width}x{height}+{x}+{y}")
        
        # Label & Entry
        Label(mainFrame, text='ID').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtID = Entry(mainFrame)
        self.txtID.grid(row=0, column=1, padx=5, pady=5)
        self.txtID.bind("<Return>", self.onCari)
        
        Label(mainFrame, text='Semester').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtSemester = tk.StringVar()
        self.CboMain = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtSemester)
        self.CboMain.grid(row=1, column=1,padx=5, pady=5)
        self.CboMain['values'] = ('Semester 1', 'Semester 2', 'Semester 3', 'Semester 4','Semester 5', 'Semester 6', 'Semester 7', 'Semester 8')
        self.CboMain.bind("<<ComboboxSelected>>", self.update_subcategories)
        self.CboMain.current()

        Label(mainFrame, text='Mata Kuliah').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtMk = tk.StringVar()
        self.CboSub1 = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtMk)
        self.CboSub1.grid(row=2, column=1,padx=5, pady=5)
        self.CboSub1.current()

        Label(mainFrame, text='SKS').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = Entry(mainFrame)
        self.txtSKS.grid(row=3, column=1, padx=5, pady=5)
        
        Label(mainFrame, text='Kelas').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtKelas = tk.StringVar()
        self.Cbokelas = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtKelas)
        self.Cbokelas.grid(row=4, column=1,padx=5, pady=5)
        self.Cbokelas['values'] = ('Kelas A', 'Kelas B', 'Kelas C', 'Kelas D', 'Kelas E', 'Kelas K', 'Kelas L')
        self.Cbokelas.current()

        # Button
        self.btnSubmit = Button(mainFrame, text='Submit', command=self.onSubmit)
        self.btnSubmit.grid(row=0, column=2, padx=5, pady=5)
        self.btnDelete = Button(mainFrame, text='Delete', command=self.onDelete)
        self.btnDelete.grid(row=1, column=2, padx=5,pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear)
        self.btnClear.grid(row=2, column=2, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onCancel)
        self.btnCancel.grid(row=3, column=2, padx=5, pady=5)
        
        # Tabel
        column = ("ID", "Semester","Mata_Kuliah", "SKS", "Kelas")
        self.tree = ttk.Treeview(mainFrame, columns=column, show='headings')
        
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width='30')
        self.tree.heading('Semester', text='Semester')
        self.tree.column('Semester', width='100')
        self.tree.heading('Mata_Kuliah', text='Mata Kuliah')
        self.tree.column('Mata_Kuliah', width='150')
        self.tree.heading('SKS', text='SKS')
        self.tree.column('SKS', width='75')
        self.tree.heading('Kelas', text='Kelas')
        self.tree.column('Kelas', width='100')
        
        # Set Position
        self.tree.place(x=0, y=200)
        self.onReload()

    def update_subcategories(self, event):
        select_subcategories = self.CboMain.get()

        self.CboSub1.set('')
        self.CboSub1['values'] = []

        if select_subcategories == 'Semester 1':
            subcategories = ['Agama', 'Matematika', 'Fisika','Bahasa Inggris','Pancasila', 'Logika Matematika', 'Dasar Algoritma dan Pemrograman', 'Praktik Dasar Algoritma dan Pemrograman', 'Pengantar Teknologi Informasi']
        elif select_subcategories == 'Semester 2':
            subcategories = ['Sistem Operasi', 'Kalkulus 1', 'Kewirausahaan Islami', 'AIK 1 (Kemanusiaan dan Keimanan)', 'Bahasa Indonesia','Kewarganegaraan','Pemrograman Terstruktur','Sistem Digital']
        elif select_subcategories == 'Semester 3':
            subcategories = ['Struktur Data dan Algoritma', 'Komunikasi Data', 'Pemrograman II (PBO)', 'Statistik dan Probabilitas', 'Arsitektur dan Organisasi Komputer', 'Sistem Informasi', 'AIK 2', 'Kalkulus 2']
        elif select_subcategories == 'Semester 4':
            subcategories = ['AIK 3','Kewirausahaan Berbasis Teknologi','Pemrograman Fungsional','Jaringan Komputer','Rekayasa Perangkat Lunak', 'Teori Bahasa Otomata', 'Pemrograman Web']
        elif select_subcategories == 'Semester 5':
            subcategories = ['Basis Data','Pemrograman Mobile','AIK 4','Metode Penelitian','Keamanan dan Keselamatan Kerja','Pemrograman Jaringan','Pemrograman Paralel']
        elif select_subcategories == 'Semester 6':
            subcategories = ['Pre Skripsi','Etika dan Profesi','Manajemen Proyek Perangkat Lunak','Rekayasa Ulang Sistem','Manajemen Jaringan','Keamanan Jaringan','Analisis Big Data']
        elif select_subcategories == 'Semester 7':
            subcategories = ['Permodelan dan Simulasi Data','Penalaran Komputer','Pemrograman Game','Desain Perangkat Lunak','Penulisan Desain Game']
        elif select_subcategories == 'Semester 8':
            subcategories = ['Kuliah Kerja Nyata','Praktek Kerja Nyata','Skripsi']
        
        self.CboSub1['values'] = subcategories
        
    def onCari(self, event=None):
        id = self.txtID.get()
        kul3 = Kuliah3()
        res = kul3.getByID(id)
        rec = kul3.affected
        if (rec>0) :
            messagebox.showinfo("Berhasil!", "Data Ditemukan")
            self.tampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Warning!", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtSKS.focus()
        return res
            
    def tampilkanData(self, event=None):
        id = self.txtID.get()
        kul3 = Kuliah3()
        res = kul3.getByID(id)
        self.txtSemester.set(kul3.semester)
        self.txtMk.set(kul3.matakuliah)
        self.txtSKS.delete(0, END)
        self.txtSKS.insert(END,kul3.sks)
        self.txtKelas.set(kul3.kelas)
        self.btnSubmit.config(text='Update')
        
    def onSubmit(self):
        id = self.txtID.get()
        semester = self.txtSemester.get()
        mata_kuliah = self.txtMk.get()
        sks = self.txtSKS.get()
        kelas = self.txtKelas.get()

        kul1 = Kuliah3()
        kul1.id = id
        kul1.semester = semester
        kul1.matakuliah = mata_kuliah
        kul1.sks = sks
        kul1.kelas = kelas
        if(self.ditemukan == True):
            res = kul1.update(id)
            ket = 'Diperbarui'
        else:
            res = kul1.simpan()
            ket = 'Disimpan'
            
        rec =kul1.affected
        if(rec>0):
            messagebox.showinfo("Information", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("Warning!", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onClear(self):
        self.txtID.delete(0,END)
        self.txtID.insert(END, "")
        self.txtSemester.set("")
        self.txtMk.set("")
        self.txtSKS.delete(0,END)
        self.txtSKS.insert(END,"")
        self.txtKelas.set("")
        self.btnClear.config(text='Clear')
        self.onReload()
        self.ditemukan = False
        
    def onReload(self):
        kul1 = Kuliah3()
        result = kul1.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        kuliah = []
        for row_data in result:
            kuliah.append(row_data)
        
        for kuliah in kuliah:
            self.tree.insert('', END, values=kuliah)

    def onDelete(self, event=None):
        id = self.txtID.get()
        kul3 = Kuliah3()
        kul3.id = id
        if(self.ditemukan==True):
            res = kul3.delete(id)
            rec = kul3.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
        
    def onCancel(self, event=None):
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
        root = tk.Tk()
        aplikasi = FrmKuliah3(root, "Data Mata Kuliah Mahasiswa", update_main_window)
        root.mainloop()


#Frm Kuliah 4
class FrmKuliah4:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry('300x200')
        self.parent.title(title)
        self.ditemukan = None
        self.parent.protocol("WM_DELETE_WINDOW", self.onCancel)
        self.aturKomponen()
        self.onReload
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 100) // 2
        y = (screen_height - 100) // 2
        width = 800
        height = 500
        self.parent.geometry(f"{width}x{height}+{x}+{y}")
        
        # Label & Entry
        Label(mainFrame, text='ID').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtID = Entry(mainFrame)
        self.txtID.grid(row=0, column=1, padx=5, pady=5)
        self.txtID.bind("<Return>", self.onCari)
        
        Label(mainFrame, text='Semester').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtSemester = tk.StringVar()
        self.CboMain = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtSemester)
        self.CboMain.grid(row=1, column=1,padx=5, pady=5)
        self.CboMain['values'] = ('Semester 1', 'Semester 2', 'Semester 3', 'Semester 4','Semester 5', 'Semester 6', 'Semester 7', 'Semester 8')
        self.CboMain.bind("<<ComboboxSelected>>", self.update_subcategories)
        self.CboMain.current()

        Label(mainFrame, text='Mata Kuliah').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtMk = tk.StringVar()
        self.CboSub1 = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtMk)
        self.CboSub1.grid(row=2, column=1,padx=5, pady=5)
        self.CboSub1.current()

        Label(mainFrame, text='SKS').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = Entry(mainFrame)
        self.txtSKS.grid(row=3, column=1, padx=5, pady=5)
        
        Label(mainFrame, text='Kelas').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtKelas = tk.StringVar()
        self.Cbokelas = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtKelas)
        self.Cbokelas.grid(row=4, column=1,padx=5, pady=5)
        self.Cbokelas['values'] = ('Kelas A', 'Kelas B', 'Kelas C', 'Kelas D', 'Kelas E', 'Kelas K', 'Kelas L')
        self.Cbokelas.current()

        # Button
        self.btnSubmit = Button(mainFrame, text='Submit', command=self.onSubmit)
        self.btnSubmit.grid(row=0, column=2, padx=5, pady=5)
        self.btnDelete = Button(mainFrame, text='Delete', command=self.onDelete)
        self.btnDelete.grid(row=1, column=2, padx=5,pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear)
        self.btnClear.grid(row=2, column=2, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onCancel)
        self.btnCancel.grid(row=3, column=2, padx=5, pady=5)
        
        # Tabel
        column = ("ID", "Semester","Mata_Kuliah", "SKS", "Kelas")
        self.tree = ttk.Treeview(mainFrame, columns=column, show='headings')
        
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width='30')
        self.tree.heading('Semester', text='Semester')
        self.tree.column('Semester', width='100')
        self.tree.heading('Mata_Kuliah', text='Mata Kuliah')
        self.tree.column('Mata_Kuliah', width='150')
        self.tree.heading('SKS', text='SKS')
        self.tree.column('SKS', width='75')
        self.tree.heading('Kelas', text='Kelas')
        self.tree.column('Kelas', width='100')
        
        # Set Position
        self.tree.place(x=0, y=200)
        self.onReload()

    def update_subcategories(self, event):
        select_subcategories = self.CboMain.get()

        self.CboSub1.set('')
        self.CboSub1['values'] = []

        if select_subcategories == 'Semester 1':
            subcategories = ['Agama', 'Matematika', 'Fisika','Bahasa Inggris','Pancasila', 'Logika Matematika', 'Dasar Algoritma dan Pemrograman', 'Praktik Dasar Algoritma dan Pemrograman', 'Pengantar Teknologi Informasi']
        elif select_subcategories == 'Semester 2':
            subcategories = ['Sistem Operasi', 'Kalkulus 1', 'Kewirausahaan Islami', 'AIK 1 (Kemanusiaan dan Keimanan)', 'Bahasa Indonesia','Kewarganegaraan','Pemrograman Terstruktur','Sistem Digital']
        elif select_subcategories == 'Semester 3':
            subcategories = ['Struktur Data dan Algoritma', 'Komunikasi Data', 'Pemrograman II (PBO)', 'Statistik dan Probabilitas', 'Arsitektur dan Organisasi Komputer', 'Sistem Informasi', 'AIK 2', 'Kalkulus 2']
        elif select_subcategories == 'Semester 4':
            subcategories = ['AIK 3','Kewirausahaan Berbasis Teknologi','Pemrograman Fungsional','Jaringan Komputer','Rekayasa Perangkat Lunak', 'Teori Bahasa Otomata', 'Pemrograman Web']
        elif select_subcategories == 'Semester 5':
            subcategories = ['Basis Data','Pemrograman Mobile','AIK 4','Metode Penelitian','Keamanan dan Keselamatan Kerja','Pemrograman Jaringan','Pemrograman Paralel']
        elif select_subcategories == 'Semester 6':
            subcategories = ['Pre Skripsi','Etika dan Profesi','Manajemen Proyek Perangkat Lunak','Rekayasa Ulang Sistem','Manajemen Jaringan','Keamanan Jaringan','Analisis Big Data']
        elif select_subcategories == 'Semester 7':
            subcategories = ['Permodelan dan Simulasi Data','Penalaran Komputer','Pemrograman Game','Desain Perangkat Lunak','Penulisan Desain Game']
        elif select_subcategories == 'Semester 8':
            subcategories = ['Kuliah Kerja Nyata','Praktek Kerja Nyata','Skripsi']
        
        self.CboSub1['values'] = subcategories
        
    def onCari(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah4()
        res = kul1.getByID(id)
        rec = kul1.affected
        if (rec>0) :
            messagebox.showinfo("Berhasil!", "Data Ditemukan")
            self.tampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Warning!", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtSKS.focus()
        return res
            
    def onDelete(self, event=None):
        id = self.txtID.get()
        kul4 = Kuliah4()
        kul4.id = id
        if(self.ditemukan==True):
            res = kul4.delete(id)
            rec = kul4.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()

    def tampilkanData(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah4()
        res = kul1.getByID(id)
        self.txtSemester.set(kul1.semester)
        self.txtMk.set(kul1.matakuliah)
        self.txtSKS.delete(0, END)
        self.txtSKS.insert(END,kul1.sks)
        self.txtKelas.set(kul1.kelas)
        self.btnSubmit.config(text='Update')
        
    def onSubmit(self):
        id = self.txtID.get()
        semester = self.txtSemester.get()
        mata_kuliah = self.txtMk.get()
        sks = self.txtSKS.get()
        kelas = self.txtKelas.get()

        kul1 = Kuliah4()
        kul1.id = id
        kul1.semester = semester
        kul1.matakuliah = mata_kuliah
        kul1.sks = sks
        kul1.kelas = kelas
        if(self.ditemukan == True):
            res = kul1.update(id)
            ket = 'Diperbarui'
        else:
            res = kul1.simpan()
            ket = 'Disimpan'
            
        rec =kul1.affected
        if(rec>0):
            messagebox.showinfo("Information", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("Warning!", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onClear(self):
        self.txtID.delete(0,END)
        self.txtID.insert(END, "")
        self.txtSemester.set("")
        self.txtMk.set("")
        self.txtSKS.delete(0,END)
        self.txtSKS.insert(END,"")
        self.txtKelas.set("")
        self.btnClear.config(text='Clear')
        self.onReload()
        self.ditemukan = False
        
    def onReload(self):
        kul1 = Kuliah4()
        result = kul1.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        kuliah = []
        for row_data in result:
            kuliah.append(row_data)
        
        for kuliah in kuliah:
            self.tree.insert('', END, values=kuliah)
        
    def onCancel(self, event=None):
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
        root = tk.Tk()
        aplikasi = FrmKuliah4(root, "Data Mata Kuliah Mahasiswa", update_main_window)
        root.mainloop()


#Frm Kuliah 5
class FrmKuliah5:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry('300x200')
        self.parent.title(title)
        self.ditemukan = None
        self.parent.protocol("WM_DELETE_WINDOW", self.onCancel)
        self.aturKomponen()
        self.onReload
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 100) // 2
        y = (screen_height - 100) // 2
        width = 800
        height = 500
        self.parent.geometry(f"{width}x{height}+{x}+{y}")
        
        # Label & Entry
        Label(mainFrame, text='ID').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtID = Entry(mainFrame)
        self.txtID.grid(row=0, column=1, padx=5, pady=5)
        self.txtID.bind("<Return>", self.onCari)
        
        Label(mainFrame, text='Semester').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtSemester = tk.StringVar()
        self.CboMain = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtSemester)
        self.CboMain.grid(row=1, column=1,padx=5, pady=5)
        self.CboMain['values'] = ('Semester 1', 'Semester 2', 'Semester 3', 'Semester 4','Semester 5', 'Semester 6', 'Semester 7', 'Semester 8')
        self.CboMain.bind("<<ComboboxSelected>>", self.update_subcategories)
        self.CboMain.current()

        Label(mainFrame, text='Mata Kuliah').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtMk = tk.StringVar()
        self.CboSub1 = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtMk)
        self.CboSub1.grid(row=2, column=1,padx=5, pady=5)
        self.CboSub1.current()

        Label(mainFrame, text='SKS').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = Entry(mainFrame)
        self.txtSKS.grid(row=3, column=1, padx=5, pady=5)
        
        Label(mainFrame, text='Kelas').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtKelas = tk.StringVar()
        self.Cbokelas = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtKelas)
        self.Cbokelas.grid(row=4, column=1,padx=5, pady=5)
        self.Cbokelas['values'] = ('Kelas A', 'Kelas B', 'Kelas C', 'Kelas D', 'Kelas E', 'Kelas K', 'Kelas L')
        self.Cbokelas.current()

        # Button
        self.btnSubmit = Button(mainFrame, text='Submit', command=self.onSubmit)
        self.btnSubmit.grid(row=0, column=2, padx=5, pady=5)
        self.btnDelete = Button(mainFrame, text='Delete', command=self.onDelete)
        self.btnDelete.grid(row=1, column=2, padx=5,pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear)
        self.btnClear.grid(row=2, column=2, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onCancel)
        self.btnCancel.grid(row=3, column=2, padx=5, pady=5)
        
        # Tabel
        column = ("ID", "Semester","Mata_Kuliah", "SKS", "Kelas")
        self.tree = ttk.Treeview(mainFrame, columns=column, show='headings')
        
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width='30')
        self.tree.heading('Semester', text='Semester')
        self.tree.column('Semester', width='100')
        self.tree.heading('Mata_Kuliah', text='Mata Kuliah')
        self.tree.column('Mata_Kuliah', width='150')
        self.tree.heading('SKS', text='SKS')
        self.tree.column('SKS', width='75')
        self.tree.heading('Kelas', text='Kelas')
        self.tree.column('Kelas', width='100')
        
        # Set Position
        self.tree.place(x=0, y=200)
        self.onReload()

    def update_subcategories(self, event):
        select_subcategories = self.CboMain.get()

        self.CboSub1.set('')
        self.CboSub1['values'] = []

        if select_subcategories == 'Semester 1':
            subcategories = ['Agama', 'Matematika', 'Fisika','Bahasa Inggris','Pancasila', 'Logika Matematika', 'Dasar Algoritma dan Pemrograman', 'Praktik Dasar Algoritma dan Pemrograman', 'Pengantar Teknologi Informasi']
        elif select_subcategories == 'Semester 2':
            subcategories = ['Sistem Operasi', 'Kalkulus 1', 'Kewirausahaan Islami', 'AIK 1 (Kemanusiaan dan Keimanan)', 'Bahasa Indonesia','Kewarganegaraan','Pemrograman Terstruktur','Sistem Digital']
        elif select_subcategories == 'Semester 3':
            subcategories = ['Struktur Data dan Algoritma', 'Komunikasi Data', 'Pemrograman II (PBO)', 'Statistik dan Probabilitas', 'Arsitektur dan Organisasi Komputer', 'Sistem Informasi', 'AIK 2', 'Kalkulus 2']
        elif select_subcategories == 'Semester 4':
            subcategories = ['AIK 3','Kewirausahaan Berbasis Teknologi','Pemrograman Fungsional','Jaringan Komputer','Rekayasa Perangkat Lunak', 'Teori Bahasa Otomata', 'Pemrograman Web']
        elif select_subcategories == 'Semester 5':
            subcategories = ['Basis Data','Pemrograman Mobile','AIK 4','Metode Penelitian','Keamanan dan Keselamatan Kerja','Pemrograman Jaringan','Pemrograman Paralel']
        elif select_subcategories == 'Semester 6':
            subcategories = ['Pre Skripsi','Etika dan Profesi','Manajemen Proyek Perangkat Lunak','Rekayasa Ulang Sistem','Manajemen Jaringan','Keamanan Jaringan','Analisis Big Data']
        elif select_subcategories == 'Semester 7':
            subcategories = ['Permodelan dan Simulasi Data','Penalaran Komputer','Pemrograman Game','Desain Perangkat Lunak','Penulisan Desain Game']
        elif select_subcategories == 'Semester 8':
            subcategories = ['Kuliah Kerja Nyata','Praktek Kerja Nyata','Skripsi']
        
        self.CboSub1['values'] = subcategories
        
    def onCari(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah5()
        res = kul1.getByID(id)
        rec = kul1.affected
        if (rec>0) :
            messagebox.showinfo("Berhasil!", "Data Ditemukan")
            self.tampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Warning!", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtSKS.focus()
        return res
            
    def tampilkanData(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah5()
        res = kul1.getByID(id)
        self.txtSemester.set(kul1.semester)
        self.txtMk.set(kul1.matakuliah)
        self.txtSKS.delete(0, END)
        self.txtSKS.insert(END,kul1.sks)
        self.txtKelas.set(kul1.kelas)
        self.btnSubmit.config(text='Update')
        
    def onSubmit(self):
        id = self.txtID.get()
        semester = self.txtSemester.get()
        mata_kuliah = self.txtMk.get()
        sks = self.txtSKS.get()
        kelas = self.txtKelas.get()

        kul1 = Kuliah5()
        kul1.id = id
        kul1.semester = semester
        kul1.matakuliah = mata_kuliah
        kul1.sks = sks
        kul1.kelas = kelas
        if(self.ditemukan == True):
            res = kul1.update(id)
            ket = 'Diperbarui'
        else:
            res = kul1.simpan()
            ket = 'Disimpan'
            
        rec =kul1.affected
        if(rec>0):
            messagebox.showinfo("Information", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("Warning!", "Data Gagal "+ket)
        self.onClear()
        return rec
    
    def onDelete(self, event=None):
        id = self.txtID.get()
        kul3 = Kuliah5()
        kul3.id = id
        if(self.ditemukan==True):
            res = kul3.delete(id)
            rec = kul3.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()

    def onClear(self):
        self.txtID.delete(0,END)
        self.txtID.insert(END, "")
        self.txtSemester.set("")
        self.txtMk.set("")
        self.txtSKS.delete(0,END)
        self.txtSKS.insert(END,"")
        self.txtKelas.set("")
        self.btnClear.config(text='Clear')
        self.onReload()
        self.ditemukan = False
        
    def onReload(self):
        kul1 = Kuliah5()
        result = kul1.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        kuliah = []
        for row_data in result:
            kuliah.append(row_data)
        
        for kuliah in kuliah:
            self.tree.insert('', END, values=kuliah)
        
    def onCancel(self, event=None):
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
        root = tk.Tk()
        aplikasi = FrmKuliah5(root, "Data Mata Kuliah Mahasiswa", update_main_window)
        root.mainloop()

#Frm Kuliah 6
class FrmKuliah6:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry('300x200')
        self.parent.title(title)
        self.ditemukan = None
        self.parent.protocol("WM_DELETE_WINDOW", self.onCancel)
        self.aturKomponen()
        self.onReload
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 100) // 2
        y = (screen_height - 100) // 2
        width = 800
        height = 500
        self.parent.geometry(f"{width}x{height}+{x}+{y}")
        
        # Label & Entry
        Label(mainFrame, text='ID').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtID = Entry(mainFrame)
        self.txtID.grid(row=0, column=1, padx=5, pady=5)
        self.txtID.bind("<Return>", self.onCari)
        
        Label(mainFrame, text='Semester').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtSemester = tk.StringVar()
        self.CboMain = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtSemester)
        self.CboMain.grid(row=1, column=1,padx=5, pady=5)
        self.CboMain['values'] = ('Semester 1', 'Semester 2', 'Semester 3', 'Semester 4','Semester 5', 'Semester 6', 'Semester 7', 'Semester 8')
        self.CboMain.bind("<<ComboboxSelected>>", self.update_subcategories)
        self.CboMain.current()

        Label(mainFrame, text='Mata Kuliah').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtMk = tk.StringVar()
        self.CboSub1 = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtMk)
        self.CboSub1.grid(row=2, column=1,padx=5, pady=5)
        self.CboSub1.current()

        Label(mainFrame, text='SKS').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = Entry(mainFrame)
        self.txtSKS.grid(row=3, column=1, padx=5, pady=5)
        
        Label(mainFrame, text='Kelas').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtKelas = tk.StringVar()
        self.Cbokelas = ttk.Combobox(mainFrame, width= 27, textvariable=self.txtKelas)
        self.Cbokelas.grid(row=4, column=1,padx=5, pady=5)
        self.Cbokelas['values'] = ('Kelas A', 'Kelas B', 'Kelas C', 'Kelas D', 'Kelas E', 'Kelas K', 'Kelas L')
        self.Cbokelas.current()

        # Button
        self.btnSubmit = Button(mainFrame, text='Submit', command=self.onSubmit)
        self.btnSubmit.grid(row=0, column=2, padx=5, pady=5)
        self.btnDelete = Button(mainFrame, text='Delete', command=self.onDelete)
        self.btnDelete.grid(row=1, column=2, padx=5,pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear)
        self.btnClear.grid(row=2, column=2, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onCancel)
        self.btnCancel.grid(row=3, column=2, padx=5, pady=5)
        
        # Tabel
        column = ("ID", "Semester","Mata_Kuliah", "SKS", "Kelas")
        self.tree = ttk.Treeview(mainFrame, columns=column, show='headings')
        
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width='30')
        self.tree.heading('Semester', text='Semester')
        self.tree.column('Semester', width='100')
        self.tree.heading('Mata_Kuliah', text='Mata Kuliah')
        self.tree.column('Mata_Kuliah', width='150')
        self.tree.heading('SKS', text='SKS')
        self.tree.column('SKS', width='75')
        self.tree.heading('Kelas', text='Kelas')
        self.tree.column('Kelas', width='100')
        
        # Set Position
        self.tree.place(x=0, y=200)
        self.onReload()

    def update_subcategories(self, event):
        select_subcategories = self.CboMain.get()

        self.CboSub1.set('')
        self.CboSub1['values'] = []

        if select_subcategories == 'Semester 1':
            subcategories = ['Agama', 'Matematika', 'Fisika','Bahasa Inggris','Pancasila', 'Logika Matematika', 'Dasar Algoritma dan Pemrograman', 'Praktik Dasar Algoritma dan Pemrograman', 'Pengantar Teknologi Informasi']
        elif select_subcategories == 'Semester 2':
            subcategories = ['Sistem Operasi', 'Kalkulus 1', 'Kewirausahaan Islami', 'AIK 1 (Kemanusiaan dan Keimanan)', 'Bahasa Indonesia','Kewarganegaraan','Pemrograman Terstruktur','Sistem Digital']
        elif select_subcategories == 'Semester 3':
            subcategories = ['Struktur Data dan Algoritma', 'Komunikasi Data', 'Pemrograman II (PBO)', 'Statistik dan Probabilitas', 'Arsitektur dan Organisasi Komputer', 'Sistem Informasi', 'AIK 2', 'Kalkulus 2']
        elif select_subcategories == 'Semester 4':
            subcategories = ['AIK 3','Kewirausahaan Berbasis Teknologi','Pemrograman Fungsional','Jaringan Komputer','Rekayasa Perangkat Lunak', 'Teori Bahasa Otomata', 'Pemrograman Web']
        elif select_subcategories == 'Semester 5':
            subcategories = ['Basis Data','Pemrograman Mobile','AIK 4','Metode Penelitian','Keamanan dan Keselamatan Kerja','Pemrograman Jaringan','Pemrograman Paralel']
        elif select_subcategories == 'Semester 6':
            subcategories = ['Pre Skripsi','Etika dan Profesi','Manajemen Proyek Perangkat Lunak','Rekayasa Ulang Sistem','Manajemen Jaringan','Keamanan Jaringan','Analisis Big Data']
        elif select_subcategories == 'Semester 7':
            subcategories = ['Permodelan dan Simulasi Data','Penalaran Komputer','Pemrograman Game','Desain Perangkat Lunak','Penulisan Desain Game']
        elif select_subcategories == 'Semester 8':
            subcategories = ['Kuliah Kerja Nyata','Praktek Kerja Nyata','Skripsi']
        
        self.CboSub1['values'] = subcategories
        
    def onCari(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah6()
        res = kul1.getByID(id)
        rec = kul1.affected
        if (rec>0) :
            messagebox.showinfo("Berhasil!", "Data Ditemukan")
            self.tampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Warning!", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtSKS.focus()
        return res
            
    def tampilkanData(self, event=None):
        id = self.txtID.get()
        kul1 = Kuliah6()
        res = kul1.getByID(id)
        self.txtSemester.set(kul1.semester)
        self.txtMk.set(kul1.matakuliah)
        self.txtSKS.delete(0, END)
        self.txtSKS.insert(END,kul1.sks)
        self.txtKelas.set(kul1.kelas)
        self.btnSubmit.config(text='Update')
        
    def onSubmit(self):
        id = self.txtID.get()
        semester = self.txtSemester.get()
        mata_kuliah = self.txtMk.get()
        sks = self.txtSKS.get()
        kelas = self.txtKelas.get()

        kul1 = Kuliah6()
        kul1.id = id
        kul1.semester = semester
        kul1.matakuliah = mata_kuliah
        kul1.sks = sks
        kul1.kelas = kelas
        if(self.ditemukan == True):
            res = kul1.update(id)
            ket = 'Diperbarui'
        else:
            res = kul1.simpan()
            ket = 'Disimpan'
            
        rec =kul1.affected
        if(rec>0):
            messagebox.showinfo("Information", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("Warning!", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onClear(self):
        self.txtID.delete(0,END)
        self.txtID.insert(END, "")
        self.txtSemester.set("")
        self.txtMk.set("")
        self.txtSKS.delete(0,END)
        self.txtSKS.insert(END,"")
        self.txtKelas.set("")
        self.btnClear.config(text='Clear')
        self.onReload()
        self.ditemukan = False

    def onDelete(self, event=None):
        id = self.txtID.get()
        kul3 = Kuliah6()
        kul3.id = id
        if(self.ditemukan==True):
            res = kul3.delete(id)
            rec = kul3.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
        
    def onReload(self):
        kul1 = Kuliah6()
        result = kul1.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        kuliah = []
        for row_data in result:
            kuliah.append(row_data)
        
        for kuliah in kuliah:
            self.tree.insert('', END, values=kuliah)
        
    def onCancel(self, event=None):
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
        root = tk.Tk()
        aplikasi = FrmKuliah6(root, "Data Mata Kuliah Mahasiswa", update_main_window)
        root.mainloop()
import tkinter as tk
from tkinter import Frame, Label, ttk, messagebox, Entry, Button, YES, BOTH, END, Tk, W
from Mahasiswa2 import *
from frmKuliah import *

class FrmMahasiswa2:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry('300x200')
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onCancel)
        self.aturKomponen()
        self.onReload
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 250) // 2
        y = (screen_height - 150) // 2
        width = 700
        height = 500
        self.parent.geometry(f"{width}x{height}+{x}+{y}")
        
        # Label & Entry
        Label(mainFrame, text='NIM').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtNIM = Entry(mainFrame)
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5)
        self.txtNIM.bind("<Return>", self.onCari)

        Label(mainFrame, text='Nama').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame)
        self.txtNama.grid(row=1, column=1, padx=5,pady=5)

        Label(mainFrame, text='Semester').grid(row=2, column=0,sticky=W, padx=5,pady=5)
        self.txtSemester = Entry(mainFrame)
        self.txtSemester.grid(row=2, column=1, padx=5, pady=5)

        Label(mainFrame, text='IP Semester').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtIPSemester = Entry(mainFrame)
        self.txtIPSemester.grid(row=3, column=1, padx=5, pady=5)

        Label(mainFrame, text='SKS').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = Entry(mainFrame)
        self.txtSKS.grid(row=4, column=1, padx=5, pady=5) 
        
        # Button
        self.btnOpen = Button(mainFrame, text='OPEN', command=self.onOpen)
        self.btnOpen.grid(row=0, column=2, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear)
        self.btnClear.grid(row=1, column=2, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onCancel)
        self.btnCancel.grid(row=3, column=2, padx=5, pady=5)
        
        # Tabel
        column = ("ID", "Nama","NIM", "Semester", "IPSemester", "SKS")
        self.tree = ttk.Treeview(mainFrame, columns=column, show='headings')
        
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width='30')
        self.tree.heading('Nama', text='Nama')
        self.tree.column('Nama', width='100')
        self.tree.heading('NIM', text='NIM')
        self.tree.column('NIM', width='100')
        self.tree.heading('Semester', text='Semester')
        self.tree.column('Semester', width='100')
        self.tree.heading('IPSemester', text='IP Semester')
        self.tree.column('IPSemester', width='100')
        self.tree.heading('SKS', text='SKS')
        self.tree.column('SKS', width='100')
        
        # Set Position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onCari(self, event=None):
        nim = self.txtNIM.get()
        mah1 = mahasiswa2()
        res = mah1.getByNIM(nim)
        rec = mah1.affected
        if(rec>0):
            messagebox.showinfo("Berhasil!", "Data Ditemukan")
            self.tampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Warning!", "Data Tidak Ditemukan")
            self.ditemukan = False
            return res
        
    def tampilkanData(self, event=None):
        nim = self.txtNIM.get()
        mah1 = mahasiswa2()
        res = mah1.getByNIM(nim)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,mah1.nama)
        self.txtSemester.delete(0,END)
        self.txtSemester.insert(END, mah1.semester)
        self.txtIPSemester.delete(0, END)
        self.txtIPSemester.insert(END, mah1.ipsemester)
        self.txtSKS.delete(0,END)
        self.txtSKS.insert(END, mah1.sks)
        
    def onClear(self):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END, "")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtSemester.delete(0,END)
        self.txtSemester.insert(END,"")
        self.txtIPSemester.delete(0,END)
        self.txtIPSemester.insert(END,"")
        self.txtSKS.delete(0,END)
        self.txtSKS.insert(END, "")
        self.btnClear.config(text='Clear')
        self.onReload()
        self.ditemukan = False
        
    def onReload(self):
        mah1 = mahasiswa2()
        result = mah1.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mahasiswa = []
        for row_data in result:
            mahasiswa.append(row_data)
        
        for mahasiswa in mahasiswa:
            self.tree.insert('', END, values=mahasiswa)

    def onOpen(self):
        new_window = tk.Toplevel(self.parent)
        if(self.txtNama.get() == 'Sodiq Abdullah'):
            FrmKuliah4(new_window, 'Data Mata Kuliah Mahasiswa', self.update_main_window)
        elif(self.txtNama.get() == 'Wahyudin'):
            FrmKuliah5(new_window,'Data Mata Kuliah Mahasiswa', self.update_main_window)
        elif(self.txtNama.get() == 'Ridho Mauliddani'):
            FrmKuliah6(new_window, 'Data Mata Kuliah Mahasiswa', self.update_main_window)
        
    def onCancel(self, event = None):
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
        root = tk.Tk()
        aplikasi = FrmMahasiswa2(root, "Data Mahasiswa", update_main_window)
        root.mainloop()
import tkinter as tk
from tkinter import Frame, Label, messagebox, Entry, Button, VERTICAL, YES, BOTH, END, Tk, W
from Dosen import *

class FromLogin:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        #self.parent.geometry('300x200')
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 250) // 2
        y = (screen_height - 150) // 2
        width = 200
        height = 180
        self.parent.geometry(f"{width}x{height}+{x}+{y}")
        
        # Label & Entry
        Label(mainFrame, text='Email', width=15).grid(row=0, column=0, sticky=W, padx=5, pady=5, columnspan=2)
        self.txtEmail = Entry(mainFrame)
        self.txtEmail.grid(row=1,column=0, padx=5, pady=5, columnspan=2)
        
        Label(mainFrame, text='Password', width=15).grid(row=2, column=0, sticky=W, padx=10, pady=10, columnspan=2)
        self.txtPassword = Entry(mainFrame)
        self.txtPassword.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
        
        #Button
        self.btnSubmit = Button(mainFrame, text='Login', command=self.onSubmit)
        self.btnSubmit.grid(row=4, column=0, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onKeluar)
        self.btnCancel.grid(row=4, column=1, padx=5, pady=5)
        
    def onSubmit(self, event=None):
        email = self.txtEmail.get()
        password = self.txtPassword.get()
        
        obj = users()
        val = obj.Validasi(email, password)
        C = val[1]
        if (C == True):
            self.update_main_window(val)
            self.parent.destroy()
            messagebox.showwarning("showwarning", "Login Berhasil")
            
        else:
            messagebox.showwarning("showwarning", "Login Gagal")
        return val
    
    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_widow(result):
        print(result)
        
        root = tk.Tk()
        aplikasi = FromLogin(root, "Login Akun", update_main_widow)
        root.mainloop()
import tkinter as tk
from tkinter import Menu, messagebox
from Frmlogin import *
from frmMahasiswa1 import *
from frmMahasiswa2 import *

class Dashboard:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('Menu')
        # self.root.attributes('-fullscreen', True)
        self.root.geometry("900x400")
        self.__data = None
        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        
        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create menus
        self.file_menu = Menu(self.menubar)
        self.guest_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)
        self.dosen1_menu = Menu(self.menubar)
        self.dosen2_menu = Menu(self.menubar)

        # add menu items to File menu
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FromLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        # add menu items to menu Admin
        self.admin_menu.add_command(label='Mahasiswa', command=lambda: self.new_window("Rental Warnet", FrmMahasiswa1))


        # add menu items to menu Mahasiswa
        self.dosen2_menu.add_command(label='Data Mahasiswa', command=lambda: self.new_window("Data Mahasiswa", FrmMahasiswa2))

        # add menu items to menu Dosen
        self.dosen1_menu.add_command(label='Data Mahasiswa', command=lambda: self.new_window("Data Mahasiswa", FrmMahasiswa1))


        # add menus to the menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def new_window(self, number, _class):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        email = self.__data[0]
        loginvalid = self.__data[1]
        index = self.file_menu.index('Login')
        # hapus menu login
        if (loginvalid == True):
            index = self.file_menu.index('Login')
            # Hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)
            
            if(email == 'saef@umc.ac.id'):
                self.menubar.add_cascade(label='Data Mahasiswa', menu=self.dosen1_menu)
            elif(email == 'tian@umc.ac.id'):
                self.menubar.add_cascade(label='Data Mahasiswa', menu=self.dosen2_menu)
            else:
                pass
                
    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FromLogin))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index('Data Mahasiswa')
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
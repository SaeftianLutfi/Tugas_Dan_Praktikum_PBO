import tkinter as tk
from tkinter import ttk, filedialog, END

def Konfirmasi():
    Hari = Hari_var.get()
    Waktu = Waktu_var.get()
    Subjek = Subjek_var.get()
    
    if Hari and Waktu and Subjek:
        Jadwal_ListBox.insert(tk.END, f"{Hari} - {Waktu}: {Subjek}")
        clear_entries()
    else:
        Error_Label.config(text="Mohon Untuk Mengisi Seluruh Kolom Yang Tersedia!")
        
def Menyimpan_Jadwal():
    file_path = filedialog.asksaveasfilename(defaulttexttension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for Jadwal in Jadwal_ListBox.get(0, END):
                file.write(Jadwal + "\n")

def Membuka_Jadwal():
    file_path = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text files", "*txt")])
    if file_path:
        with open(file_path, "r") as file:
            Jadwal2 = file.readlines()
            for Jadwal in Jadwal2:
                Jadwal_ListBox.insert(END, Jadwal.strip())
            
def clear_entries():
    Hari_var.set("")
    Waktu_var.set("")
    Subjek_Entry.delete(0, END)
    Error_Label.config(text="")
    
# Membuat Window
root = tk.Tk()
root.title("Jadwal Mata Kuliah")

# Variabel StringVar untuk menyimpan input dari pengguna
Hari_var = tk.StringVar(root)
Waktu_var = tk.StringVar(root)
Subjek_var = tk.StringVar(root)

# Label dan Entry untuk Hari
Hari_Label = tk.Label(root, text="Hari:")
Hari_Label.grid(row=0, column=0, padx=10, pady=10)
Hari_Entry = ttk.Combobox(root, width=30, textvariable=Hari_var, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
Hari_Entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

# Label dan Entry untuk Waktu
Waktu_Label = tk.Label(root, text="Waktu:")
Waktu_Label.grid(row=1, column=0, padx=10, pady=10)
Waktu_Entry = ttk.Combobox(root, width=30, textvariable=Waktu_var, values=["09.30-12.00", "10.31-12.10", "13.00-15.30", 
                                    "15.00-16.40", "09.30-11.00", "09.41-12.10", "08.00-09.40", "09.41-11.20"])
Waktu_Entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Label dan Entry untuk Mata Kuliah
Subjek_Label = tk.Label(root, text="Mata Kuliah")
Subjek_Label.grid(row=2, column=0, padx=10, pady=10)
Subjek_Entry = ttk.Combobox(root, width=30, textvariable=Subjek_var, values=["Pemrograman II (PBO)", "Statistik dan Probabilitas", 
                "Arsitektur dan Organisasi Komputer","Komunikasi Data", "Sistem Informasi(APSI)",
                "Struktur Data dan Algoritma", "AIK 2 (Ibadah, Akhlak dan Muamalah)", "Kalkulus II"])
Subjek_Entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

# Button Konfirmasi
Submit_Button = tk.Button(root, text="Add", width=10, command=Konfirmasi)
Submit_Button.grid(row=3, column=0, padx=10, pady=10)

# Label Untuk Pesan Kesalahan Operasi
Error_Label = tk.Label(root, text="", fg="red")
Error_Label.grid(row=4, column=0, columnspan=3, pady=10)

# ListBox Untuk Menampilkan Jadwal
Jadwal_ListBox = tk.Listbox(root, width=50, height=10)
Jadwal_ListBox.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Save Button
Save_Button = tk.Button(root, text="Save", width=10, command=Menyimpan_Jadwal)
Save_Button.grid(row=3, column=2, padx=10, pady=10)

# Open Button
Open_Button = tk.Button(root, text="Open", width=10, command=Membuka_Jadwal)
Open_Button.grid(row=3, column=1, padx=10, pady=10)

# Nama, NIM dan Kelas
frame = tk.Frame(root)
frame.grid(padx=10, pady=10)

nametag = tk.Frame(frame, bg="lightblue", height=30)
nametag.grid(row=6, column=0, columnspan=3, sticky='ew', padx=10, pady=10)

nama = tk.Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
nama.grid(row=6, column=0, sticky='ew', padx=10, pady=10)

nim = tk.Label(nametag, text="220511078", bg='lightblue')
nim.grid(row=6, column=1, sticky='ew', padx=10, pady=10)

kelas = tk.Label(nametag, text="TIF22E", bg='lightblue' ) 
kelas.grid(row=6, column=2, sticky='ew', padx=10, pady=10)


# Menjalankan loop utama
root.mainloop()
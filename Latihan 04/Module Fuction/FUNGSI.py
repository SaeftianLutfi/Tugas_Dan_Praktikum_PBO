import tkinter as tk
from tkinter import END,Frame,Label,Entry,Button,W
import math

# Fungsi Rumus Balok
def Luas_Balok(txtPanjang,txtLebar,txtTinggi, txtLuas_Balok):
    Panjang = float(txtPanjang.get())
    Lebar = float(txtLebar.get())
    Tinggi = float(txtTinggi.get())

    Luas = 2 * (Panjang * Lebar + Panjang * Tinggi + Lebar * Tinggi)

    txtLuas_Balok.delete(0,END)
    txtLuas_Balok.insert(END,Luas)
    
def Volume_Balok(txtPanjang,txtLebar,txtTinggi, txtVolume_Balok):
    Panjang = float(txtPanjang.get())
    Lebar = float(txtLebar.get())
    Tinggi = float(txtTinggi.get())
    
    Volume = Panjang * Lebar * Tinggi

    txtVolume_Balok.delete(0,END)
    txtVolume_Balok.insert(END, Volume)

# Fungsi Rumus Kubus
def Luas_Kubus(txtSisi, txtLuas_Kubus):
    Sisi = float(txtSisi.get())
    
    Luas_Kubus = 6 * Sisi ** 2
    
    txtLuas_Kubus.delete(0,END)
    txtLuas_Kubus.insert(END, Luas_Kubus)

def Volume_Kubus(txtSisi, txtVolume_Kubus):
    Sisi = float(txtSisi.get())
    
    Volume_Kubus = Sisi ** 3
    
    txtVolume_Kubus.delete(0,END)
    txtVolume_Kubus.insert(END, Volume_Kubus)

# Fungsi Rumus Bola
def Luas_Bola(txtr, txtLuas_Bola):
    r = float(txtr.get())
    
    Luas_Bola = 4 * math.pi * r ** 2
    
    txtLuas_Bola.delete(0,END)
    txtLuas_Bola.insert(END, Luas_Bola)

def Volume_Bola(txtr, txtVolume_Bola):
    r = float(txtr.get())
    
    Volume_Bola = (4/3) * math.pi * r**3
    
    txtVolume_Bola.delete(0,END)
    txtVolume_Bola.insert(END, Volume_Bola)

# Fungsi Rumus Kerucut
def Garis_Pelukis(txtr, txtTinggi, txtGaris_Pelukis):
    r = float(txtr.get())
    Tinggi = float(txtTinggi.get())
    
    Garis_Pelukis = math.sqrt(r ** 2 + Tinggi ** 2)
    
    txtGaris_Pelukis.delete(0,END)
    txtGaris_Pelukis.insert(END, Garis_Pelukis)

def Luas_Kerucut(txtr, txtGaris_Pelukis, txtLuas_Kerucut):
    r = float(txtr.get())
    Garis_Pelukis = float(txtGaris_Pelukis.get())
    
    Luas_Kerucut = math.pi * r * (r*Garis_Pelukis)
    
    txtLuas_Kerucut.delete(0,END)
    txtLuas_Kerucut.insert(END, Luas_Kerucut)

def Volume_Kerucut(txtr, txtTinggi, txtVolume_Kerucut):
    r = float(txtr.get())
    Tinggi = float(txtTinggi.get())
    
    Volume_Kerucut = (1/3) * math.pi * r ** 2 * Tinggi
    
    txtVolume_Kerucut.delete(0,END)
    txtVolume_Kerucut.insert(END, Volume_Kerucut)

# Fungsi Rumus Limas Segiempat
def Luas_Limas_Segiempat(txtPanjang, txtLebar, txtTinggi_alas, txtLuas_Limas_Segiempat):
    Panjang = float(txtPanjang.get())
    Lebar = float(txtLebar.get())
    Tinggi_alas = float(txtTinggi_alas.get())
    
    Luas_Limas_Segiempat = Panjang * Lebar + 2 * Panjang * Tinggi_alas + 2 * Lebar * Tinggi_alas
    
    txtLuas_Limas_Segiempat.delete(0,END)
    txtLuas_Limas_Segiempat.insert(END, Luas_Limas_Segiempat)

def Volume_Limas_Segiempat(txtPanjang, txtLebar, txtTinggi, txtVolume_Limas_Segiempat):
    Panjang = float(txtPanjang.get())
    Lebar = float(txtLebar.get())
    Tinggi = float(txtTinggi.get())
    
    Volume_Limas_Segiempat = (1/3) * Panjang * Lebar * Tinggi
    
    txtVolume_Limas_Segiempat.delete(0,END)
    txtVolume_Limas_Segiempat.insert(END, Volume_Limas_Segiempat)

# Fungsi Rumus Limas Segitiga
def Luas_Segitiga(txtPanjang, txtTinggi_Segitiga_Dasar, txtLuas_Segitiga):
    Panjang = float(txtPanjang.get())
    Tinggi_Segitiga_Dasar = float(txtTinggi_Segitiga_Dasar.get())
    
    Luas_Segitiga = 0.5 * Panjang * Tinggi_Segitiga_Dasar
    
    txtLuas_Segitiga.delete(0,END)
    txtLuas_Segitiga.insert(END, Luas_Segitiga)

def Keliling_Segitiga(txtPanjang, txtKeliling_Segitiga):
    Panjang = float(txtPanjang.get())
    
    Keliling_Segitiga = 3 * Panjang
    
    txtKeliling_Segitiga.delete(0,END)
    txtKeliling_Segitiga.insert(END,Keliling_Segitiga)

def Luas_Permukaan_Limas_Segitiga(txtTinggi_Limas, txtLuas_Segitiga, txtKeliling_Segitiga, txtLuas_Permukaan_Limas_Segitiga):
    Tinggi_Limas = float(txtTinggi_Limas.get())
    Keliling_Segitiga = float(txtKeliling_Segitiga.get())
    Luas_Segitiga = float(txtLuas_Segitiga.get())
    
    Luas_Permukaan_Limas_Segitiga = Luas_Segitiga + (1/2) * Keliling_Segitiga * Tinggi_Limas
    
    txtLuas_Permukaan_Limas_Segitiga.delete(0,END)
    txtLuas_Permukaan_Limas_Segitiga.insert(END,Luas_Permukaan_Limas_Segitiga)

def Volume_Limas_Segitiga(txtLuas_Segitiga, txtTinggi_Limas, txtVolume_Limas_Segitiga):
    Luas_Segitiga = float(txtLuas_Segitiga.get())
    Tinggi_Limas = float(txtTinggi_Limas.get())
    
    Volume_Limas_Segitiga = (1/3) * Luas_Segitiga * Tinggi_Limas
    
    txtVolume_Limas_Segitiga.delete(0,END)
    txtVolume_Limas_Segitiga.insert(END, Volume_Limas_Segitiga)

# Fungsi Rumus Prisma Segitiga
def Luas_Segitiga(txtPanjang, txtTinggi_Segitiga_Dasar, txtLuas_Segitiga):
    Panjang = float(txtPanjang.get())
    Tinggi_Segitiga_Dasar = float(txtTinggi_Segitiga_Dasar.get())
    
    Luas_Segitiga = 0.5 * Panjang *Tinggi_Segitiga_Dasar
    
    txtLuas_Segitiga.delete(0,END)
    txtLuas_Segitiga.insert(END, Luas_Segitiga)

def Keliling_Segitiga(txtPanjang, txtKeliling_Segitiga):
    Panjang = float(txtPanjang.get())
    
    Keliling_Segitiga = 3 * Panjang
    
    txtKeliling_Segitiga.delete(0,END)
    txtKeliling_Segitiga.insert(END,Keliling_Segitiga)

def Luas_Permukaan_Prisma_Segitiga(txtLuas_Segitiga, txtKeliling_Segitiga, txtTinggi_Prisma, txtLuas_Permukaan_Prisma_Segitiga):
    Luas_Segitiga = float(txtLuas_Segitiga.get())
    Keliling_Segitiga = float(txtKeliling_Segitiga.get())
    Tinggi_Prisma = float(txtTinggi_Prisma.get())
    
    Luas_Permukaan_Prisma_Segitiga = 2 * Luas_Segitiga + Keliling_Segitiga * Tinggi_Prisma
    
    txtLuas_Permukaan_Prisma_Segitiga.delete(0,END)
    txtLuas_Permukaan_Prisma_Segitiga.insert(END,Luas_Permukaan_Prisma_Segitiga)

def Volume_Prisma_Segitiga(txtLuas_Segitiga, txtTinggi_Prisma, txtVolume_Prisma_Segitiga):
    Luas_Segitiga = float(txtLuas_Segitiga.get())
    Tinggi_Prisma = float(txtTinggi_Prisma.get())
    
    Volume_Prisma_Segitiga = Luas_Segitiga * Tinggi_Prisma
    
    txtVolume_Prisma_Segitiga.delete(0,END)
    txtVolume_Prisma_Segitiga.insert(END,Volume_Prisma_Segitiga)    

# Fungsi Rumus Silinder (Tabung)
def Luas_Permukaan_Tabung(txtr, txtTinggi, txtLuas_Permukaan_Tabung):
    r = float(txtr.get())
    Tinggi = float(txtTinggi.get())
    
    Luas_Permukaan_Tabung = 2 * math.pi * r * (r + Tinggi)
    
    txtLuas_Permukaan_Tabung.delete(0,END)
    txtLuas_Permukaan_Tabung.insert(END, Luas_Permukaan_Tabung)

def Volume_Tabung(txtr, txtTinggi, txtVolume_Tabung):
    r = float(txtr.get())
    Tinggi = float(txtTinggi.get())
    
    Volume_Tabung = math.pi * r ** 2 * Tinggi
    
    txtVolume_Tabung.delete(0,END)
    txtVolume_Tabung.insert(END, Volume_Tabung)
    
# Fungsi Rumus Persegi Panjang
def Luas_Persegi_Panjang(txtPanjang, txtLebar, txtLuas_Persegi_Panjang):
    Panjang = float(txtPanjang.get())
    Lebar = float(txtLebar.get())
    
    Luas_Persegi_Panjang = Panjang * Lebar
    
    txtLuas_Persegi_Panjang.delete(0,END)
    txtLuas_Persegi_Panjang.insert(END,Luas_Persegi_Panjang)

def Keliling_Persegi_Panjang(txtPanjang, txtLebar, txtKeliling_Persegi_Panjang):
    Panjang = float(txtPanjang.get())
    Lebar = float(txtLebar.get())
    
    Keliling_Persegi_Panjang = (2 * Panjang) + (2 * Lebar)
    
    txtKeliling_Persegi_Panjang.delete(0,END)
    txtKeliling_Persegi_Panjang.insert(END,Keliling_Persegi_Panjang)   
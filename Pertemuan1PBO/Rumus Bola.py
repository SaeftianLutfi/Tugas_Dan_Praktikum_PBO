print("Rumus Bola")

# Import modul math untuk konstanta pi (π)
import math

# Input jari-jari bola (r)
r = float(input("Masukkan jari-jari bola: "))

# Menghitung luas permukaan bola
Luas_Permukaan = 4 * math.pi * r ** 2

# Menghitung volume bola
Volume = (4/3) * math.pi * r**3

# Menampilkan hasil
print("Luas permukaan bola adalah:", Luas_Permukaan)
print("Volume bola adalah:", Volume)
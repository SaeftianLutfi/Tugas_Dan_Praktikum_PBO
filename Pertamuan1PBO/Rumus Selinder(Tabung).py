print("Rumus Selinder (Tabung)")

# Import modul math untuk konstanta pi (π)
import math

# Input jari-jari tabung (r) dan tinggi tabung (T)
r = float(input("Masukkan jari-jari tabung: "))
T = float(input("Masukkan tinggi tabung: "))

# Menghitung luas permukaan silinder
luas_permukaan = 2 * math.pi * r * (r + T)

# Menghitung volume silinder
volume = math.pi * r ** 2 * T

# Menampilkan hasil
print("Luas permukaan silinder adalah:", luas_permukaan)
print("Volume silinder adalah:", volume)
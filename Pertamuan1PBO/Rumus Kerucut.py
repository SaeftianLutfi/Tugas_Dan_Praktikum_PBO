print("Rumus Kerucut")

# Import modul math untuk konstanta pi (π) dan akar kuadrat
import math

# Input jari-jari kerucut (r) dan tinggi kerucut (T)
r = float(input("Masukkan jari-jari kerucut: "))
T = float(input("Masukkan tinggi kerucut: "))

# Menghitung garis pelukis kerucut (s)
s = math.sqrt(r ** 2 + T ** 2)

# Menghitung luas permukaan kerucut
luas_permukaan = math.pi * r * (r + s)

# Menghitung volume kerucut
volume = (1/3) * math.pi * r**2 * T

# Menampilkan hasil
print("Luas permukaan kerucut adalah:", luas_permukaan)
print("Volume kerucut adalah:", volume)
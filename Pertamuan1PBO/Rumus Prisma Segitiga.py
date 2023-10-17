print("Rumus Prisma Segitiga")

# Import modul math untuk menghitung akar kuadrat (pada kasus menghitung keliling segitiga)
import math

# Input panjang sisi segitiga dasar (A), tinggi segitiga dasar (T), dan tinggi prisma (TP)
A = float(input("Masukkan panjang sisi segitiga dasar (A): "))
T = float(input("Masukkan tinggi segitiga dasar (T): "))
TP = float(input("Masukkan tinggi prisma (TP): "))

# Menghitung luas segitiga dasar
luas_segitiga = 0.5 * A * T

# Menghitung keliling segitiga dasar
keliling_segitiga = 3 * A

# Menghitung luas permukaan prisma segitiga
luas_permukaan = 2 * luas_segitiga + keliling_segitiga * TP

# Menghitung volume prisma segitiga
volume = luas_segitiga * TP

# Menampilkan hasil
print("Luas permukaan prisma segitiga adalah:", luas_permukaan)
print("Volume prisma segitiga adalah:", volume)
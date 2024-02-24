import math
print("Rumus Kerucut")

# Input Jari-jari, Sisi dan Tinggi
r = float(input("Masukkan Jari-jari:"))
Tinggi = float(input("Masukkan Tinggi:"))

# Menghitung Garis Pelukis
s = math.sqrt (r ** 2 + Tinggi ** 2)

# Menghitung Luas Permukaan
Luas = math.pi * r * (r + s)

# Menghitung Volume 
Volume = 1/3 * math.pi * r ** 2 * Tinggi

# Menampilkan Hasil
print("Luas Selimut Kerucut:", s)
print("Luas Kerucut:", Luas)
print("Volume Kerucut:", Volume)
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
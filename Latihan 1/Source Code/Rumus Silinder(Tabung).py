import math
print("Rumus Silinder (Tabung)")

# Input Tinggi dan Jari-jari Tabung
Tinggi = float(input("Masukkan Tinggi Tabung:"))
r = float(input("Masukkan Jari-Jari Tabung:"))

# Menghitung Luas Tabung
Luas = 2 * math.pi * r * (r + Tinggi)

# Menghitung Volume Tabung
Volume = math.pi * r ** 2 * Tinggi

# Menampilkan Hasil
print("Luas Permukaan Tabung:", Luas)
print("Volume Tabung:", Volume)
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
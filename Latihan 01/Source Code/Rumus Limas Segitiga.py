import math
print("Rumus Limas Segitiga")

# Input Luas Segitiga, Alas, Tinggi Segitiga dan Tinggi Limas
A = float(input("Masukkan Panjang Sisi Segitiga Dasar:"))
TSD = float(input("Masukkan Tinggi Segitiga Dasar:"))
TL = float(input("Masukkan Tinggi Limas:"))
TA = float(input("Masukkan Tinggi Segitiga Alas:"))

# Menghitung Segitiga
Luas_Segitiga = 0.5 * A * TSD

# Menghitung Keliling Segitiga
Keliling_Segitiga = 3 * A

# Menghitung Luas Limas Segitiga
Luas = Luas_Segitiga + (1/2) * Keliling_Segitiga * TL

# Menghitung Volume Limas Segitiga
Volume = (1/3) * Luas_Segitiga * TL

# Menampilkan Hasil
print("Luas Limas Segitiga:", Luas)
print("Volume Limas Segitiga:", Volume)
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
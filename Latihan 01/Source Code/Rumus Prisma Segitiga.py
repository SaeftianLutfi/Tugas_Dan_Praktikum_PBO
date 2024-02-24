print("Rumus Prisma SegiTiga")

# Input Sisi, Tinggi, Alas, Tinggi Segitiga
A = float(input("Masukkan Panjang Sisi Segitiga Dasar:"))
T = float(input("Masukkan Tinggi Segitiga Dasar:"))
TP = float(input("Masukkan Tinggi Prisma:"))

# Menghitung Luas Segitiga
Luas_Segitiga = 0.5 * A * T

# Menghitung Keliling Segitiga
Keliling_Segitiga = 3 * A

# Menghitung Luas Permukaan Prisma Segitiga
Luas = 2 * Luas_Segitiga + Keliling_Segitiga * TP

# Menghitung Volume Prisma Segitiga
Volume = Luas_Segitiga * TP

# Menampilkan Hasil
print("Luas Prisma Segitiga:", Luas)
print("Volume Prisma Segitiga:", Volume)
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
print("Rumus Balok")

# Input Panjang, Lebar, dan Tinggi Balok
Panjang = float(input("Masukkan Panjang Balok:"))
Lebar = float(input("Masukkan Lebar Balok:"))
Tinggi = float(input("Masukkan Tinggi Balok:"))

# Menghitung Luas Permukaan Balok
Luas = (2 * Panjang * Lebar) + (2 * Panjang * Tinggi) + (2 * Lebar * Tinggi)

# Menghitung Volume Balok
Volume = Panjang * Lebar * Tinggi

# Menampilkan Hasil
print("Luas Balok:", Luas)
print("Volume Balok:", Volume)
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
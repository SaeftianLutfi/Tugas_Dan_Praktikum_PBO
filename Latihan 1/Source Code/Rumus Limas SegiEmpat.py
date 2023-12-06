print("Rumus Limas SegiEmpat")

# Input Luas Sisi dan Tinggi Limas SegiEmpat
PA = float(input("Masukkan Panjang Alas:"))
LA = float(input("Masukkan Luas Alas:"))
Tinggi = float(input("Masukkan Tinggi Limas:"))
TSA = float(input("Masukkan Tinggi Segitiga Alas:"))

# Menhitung Luas Alas Limas SegiEmpat
Luas = PA * LA + 2 * PA * TSA + 2 * LA * TSA

# Menghitung Volume Limas SegiEmpat
Volume = 1/3 * PA * LA * Tinggi

# Menampilkan Hasil
print("Luas Limas SegiEmpat:", Luas)
print("Volume Limas SegiEmpat:", Volume)
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
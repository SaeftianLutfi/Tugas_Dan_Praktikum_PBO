print("Rumus Balok")

# Input panjang, lebar, dan tinggi balok
Panjang = float(input("Masukkan panjang balok: "))
Lebar = float(input("Masukkan lebar balok: "))
Tinggi = float(input("Masukkan tinggi balok: "))

# Menghitung luas permukaan balok
Luas_Permukaan = 2 * (Panjang * Lebar + Panjang * Tinggi + Lebar * Tinggi)

# Menghitung volume balok
Volume = Panjang * Lebar * Tinggi

# Menampilkan hasil
print("Luas permukaan balok adalah:", Luas_Permukaan)
print("Volume balok adalah:", Volume)
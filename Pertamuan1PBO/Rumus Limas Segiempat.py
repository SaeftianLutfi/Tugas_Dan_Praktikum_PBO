print("Rumus Limas Segiempat")

# Input Panjang Alas, Lebar Alas, Tinggi Limas, dan Tinggi Segitiga Alas
Panjang_Alas = float(input("Masukkan panjang alas : "))
Lebar_Alas = float(input("Masukkan lebar alas : "))
Tinggi = float(input("Masukkan tinggi limas : "))
Tinggi_Segitiga_Alas = float(input("Masukkan tinggi segitiga alas : "))

# Menghitung Luas Permukaan Limas Segi Empat
Luas_Permukaan = Panjang_Alas * Lebar_Alas + 2 * Panjang_Alas * Tinggi_Segitiga_Alas + 2 * Lebar_Alas * Tinggi_Segitiga_Alas

# Menghitung volume limas segi empat
Volume = (1/3) * Panjang_Alas * Lebar_Alas * Tinggi

# Menampilkan hasil
print("Luas permukaan limas segi empat adalah:", Luas_Permukaan)
print("Volume limas segi empat adalah:", Volume)
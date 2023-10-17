print("Rumus Limas Segitiga")

# Import modul math untuk menghitung akar kuadrat (pada kasus menghitung keliling segitiga)
import math

# Input panjang sisi segitiga dasar (a), tinggi segitiga dasar (h), tinggi limas (H), dan tinggi segitiga alas (H_alas)
A = float(input("Masukkan panjang sisi segitiga dasar (A): "))
TSD = float(input("Masukkan tinggi segitiga dasar (TSD): "))
TL = float(input("Masukkan tinggi limas (TL): "))
TA = float(input("Masukkan tinggi segitiga alas (TA): "))

# Menghitung luas segitiga dasar
luas_segitiga = 0.5 * A * TSD

# Menghitung keliling segitiga dasar
keliling_segitiga = 3 * A

# Menghitung luas permukaan limas segitiga
Luas_Permukaan = luas_segitiga + (1/2) * keliling_segitiga * TL

# Menghitung volume limas segitiga
Volume = (1/3) * luas_segitiga * TL

# Menampilkan hasil
print("Luas permukaan limas segitiga adalah:", Luas_Permukaan)
print("Volume limas segitiga adalah:", Volume)
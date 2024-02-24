print("Konversi Suhu Fahrenheit")
def get_celcius(suhu):
    C = 5/9 * (float(suhu) - 32)
    return C

def get_reamur(suhu):
    R = 4/9 * (float(suhu) - 32)
    return R

def get_kelvin(suhu):
    K = 5/9 * (float(suhu) - 32) + 273
    return K

# Entry
suhu = input("Masukkan Suhu Dalam Fahrenheit:")

# Rumus
C = get_celcius(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)

# Output
print(str(C) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")

# Nama, NIM dan Kelas
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
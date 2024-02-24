print("Konversi Suhu Kelvin")
def get_celcius(suhu):
    C = float(suhu) - 273
    return C

def get_fahrenheit(suhu):
    F = 9/5 * (float(suhu) - 273) + 32
    return F

def get_reamur(suhu):
    R = 4/5 * (float(suhu) - 273)
    return R

# Entry
suhu = input("Masukkan Suhu Dalam Kelvin:")

# Rumus
C = get_celcius(suhu)
F = get_fahrenheit(suhu)
R = get_reamur(suhu)

# Output
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")

# Nama, NIM dan Kelas
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
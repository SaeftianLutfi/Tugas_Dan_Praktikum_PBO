print("Konversi Suhu Kelvin")
class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_Kelvin(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = self.suhu - 273
        return val
    
    def get_fahrenheit(self):
        val = 4/5 * (self.suhu - 273) + 32
        return val
    
    def get_reamur(self):
        val = 4/5 * (self.suhu - 273)
        return val
    
suhu = input ("Masukkan Suhu Dalam Kelvin:")
K = Kelvin(float(suhu))
val = K.get_celcius()

C = K.get_celcius()
F = K.get_fahrenheit()
R = K.get_reamur()

print(str(val) + " Kelvin, sama dengan: ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")

# Nama, NIM dan Kelas
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
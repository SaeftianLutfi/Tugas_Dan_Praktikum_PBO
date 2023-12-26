print("Konversi Suhu Reamur")
class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_reamur(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = 5/4 * self.suhu
        return val
    
    def get_fahrenheit(self):
        val = (9/4 * self.suhu) + 32
        return val
    
    def get_kelvin(self):
        val = 5/4 * self.suhu + 273
        return val
    
suhu = input ("Masukkan Suhu Dalam Reamur:")
R = Reamur(float(suhu))
val = R.get_celcius()

C = R.get_fahrenheit()
F = R.get_reamur()
K = R.get_kelvin()

print(str(val) + " Reamur, sama dengan: ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")

# Nama, NIM dan Kelas
print("\nNama: Saeftian Lutfi")
print("NIM: 220511078")
print("Kelas: TIF22E / R5")
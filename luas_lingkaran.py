import math

# Mengambil input dari pengguna untuk jari-jari lingkaran
r = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas lingkaran
luas = math.pi * r**2

# Menghitung keliling lingkaran
keliling = 2 * math.pi * r

# Menampilkan hasil dengan dua digit desimal
print(f"Luas lingkaran: {luas:.2f}")
print(f"Keliling lingkaran: {keliling:.2f}")
a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")

# Mengubah input string ke integer
a = int(a)
b = int(b)

print("Variable a =", a)
print("Variable b =", b)

# Menggabungkan nilai a dan b
hasil_gabungan = a + b
print("Hasil penggabungan {} & {} = {}".format(a, b, hasil_gabungan))

# Menambahkan nilai a dan b
hasil_penjumlahan = a + b
print("Hasil penjumlahan {} + {} = {}".format(a, b, hasil_penjumlahan))

# Membagi nilai a dengan b
hasil_pembagian = a / b
print("Hasil pembagian {} / {} = {:.2f}".format(a, b, hasil_pembagian))

# Praktikum 3

## Latihan 1

- Penggunaan End:
  Kode ini mencetak beberapa huruf (A, B, C) berturut-turut tanpa spasi atau baris baru di antara mereka. Dengan kata lain, huruf-huruf ini akan dicetak tanpa jeda, karena argumen end='' digunakan. Setelah cetakan huruf-huruf itu selesai, ada print() kosong untuk mencetak baris baru dan mengakhiri baris tersebut. Lalu, cetak 'X', 'Y', 'Z' pada baris baru masing-masing.

- Penggunaan Separator: Kode ini mendefinisikan beberapa variabel (w, x, y, z) dan mencetak nilai-nilainya. Penggunaan sep digunakan untuk menentukan pemisah antara nilai-nilai yang dicetak. Contohnya, print(w, x, y, z, sep=',') akan mencetak nilai-nilai tersebut dipisahkan oleh koma.

- String Format: Kode ini mencetak nilai-nilai yang ditingkatkan secara eksponensial dengan format {0} {1}. Pada baris ini, Anda bisa melihat bahwa nilai ke-0 adalah 10 pangkat 0, nilai ke-1 adalah 10 pangkat 1, dan seterusnya. Ini digunakan untuk menunjukkan penggunaan format string sederhana.

- String Format (dengan padding): Kode ini mencetak nilai-nilai yang ditingkatkan secara eksponensial dengan format {0:>3} {1:>16}. Format ini menambahkan pemformatan tambahan ke cetakan, seperti penambahan spasi untuk membuat lebar cetakan menjadi 3 karakter untuk angka pertama dan 16 karakter untuk angka kedua.

## Latihan 2

- Program ini meminta pengguna untuk memasukkan nilai a dan b menggunakan input(). Ini memungkinkan pengguna untuk memasukkan nilai secara interaktif.

- Selanjutnya, nilai a dan b yang diterima dari input() diubah dari tipe data string menjadi integer menggunakan int(a) dan int(b). Hal ini dilakukan agar nilai-nilai tersebut dapat digunakan dalam operasi matematika.

- Program mencetak nilai a dan b setelah konversi dalam format "Variable a = [nilai_a]" dan "Variable b = [nilai_b]".

- Kemudian, program menggabungkan nilai a dan b dengan operasi penjumlahan dan mencetak hasilnya dalam format "Hasil penggabungan [nilai_a] & [nilai_b] = [hasil_gabungan]".

- Program juga melakukan operasi penjumlahan antara a dan b dan mencetak hasilnya dalam format "Hasil penjumlahan [nilai_a] + [nilai_b] = [hasil_penjumlahan]".

- Terakhir, program melakukan operasi pembagian antara a dan b, dan hasilnya diformat agar hanya memiliki dua angka desimal dengan menggunakan :.2f. Hasil pembagian ini dicetak dalam format "Hasil pembagian [nilai_a] / [nilai_b] = [hasil_pembagian]".

## Latihan 3

- Program ini akan mencetak output yang berbentuk belah ketupat

- Pengguna diminta untuk memasukkan lebar belah ketupat dengan lebar_belah_ketupat = int(input('Input lebar belah ketupat: ')). Nilai yang dimasukkan akan digunakan untuk menentukan lebar belah ketupat.

- Selanjutnya, program menggunakan dua loop for untuk menghasilkan pola belah ketupat. Loop pertama digunakan untuk bagian atas belah ketupat, dan loop kedua untuk bagian bawah.

- Dalam loop pertama, program mencetak spasi sebanyak (lebar_belah_ketupat - i) diikuti oleh tanda '\*' sebanyak (i+1), menciptakan pola belah ketupat bagian atas.

- Dalam loop kedua, program mencetak spasi sebanyak (i+1) diikuti oleh tanda '\*' sebanyak (lebar_belah_ketupat - i), menciptakan pola belah ketupat bagian bawah.

## menghitung luas dan keliling Lingkaran Menggunakan Python

- Jika menggunakan arch based linux bisa dengan command

```
python -m venv venv
```

```
source venv/bin/activate
```

- Program ini menggunakan modul math untuk mengakses nilai π (pi) yang digunakan dalam perhitungan lingkaran.

Pengguna diminta untuk memasukkan jari-jari lingkaran dengan perintah input, dan input tersebut diubah menjadi angka desimal (float) dengan float(input("Masukkan jari-jari lingkaran: ")).

Selanjutnya, program menghitung luas lingkaran dengan rumus luas = π * r^2 dan menyimpan hasilnya dalam variabel luas.

Program juga menghitung keliling lingkaran dengan rumus keliling = 2 * π * r dan menyimpan hasilnya dalam variabel keliling.

Hasil perhitungan luas dan keliling lingkaran kemudian ditampilkan kepada pengguna dengan menggunakan print. {luas:.2f} dan {keliling:.2f} digunakan untuk memformat hasil dengan dua digit desimal.

## Langkah-langkah pengerjaan latihan

1. Konfigurasi terlebih dahulu username dan email pada global repository-nya

```
git config --global user.name “nama_user”
```

```
git config --global user.email “email_user”
```

2. Buat repository local

```
mkdir bahasa_pemrograman
```

```
cd bahasa_pemrograman
```

```
mkdir lab2py
```

3. Jika sudah, jalankan command (command git init digunakan untuk menginisialisasi repositori git baru)

```
git init
```

## Menambahkan File Baru Pada Repository Lokal

1. Untuk membuat file baru bisa juga dengan text editor

disini akan menggunakan terminal

```
echo “# lab2py” >> README.md
```

2. Untuk menambahkan file yang baru saja dibuat, gunakan command

```
git add README.md
```

3. Untuk menyimpan perubahan yang ada pada database repositori
   lokal, gunakan command

```
git commit -m "first commit"
```

## Membuat Repository Server

1. Server repository yang digunakan adalah github
2. Buat akun github terlebih dahulu
3. Klik tombol + new repository
4. Isi nama repository-nya,

```
   contoh: lab2py
```

5. lalu klik tombol Create repository

## Menambahkan Remote Repository

- Remote Repository merupakan server repositori yang akan digunakan untuk menyimpan segala perubahan yang dilakukan pada repositori lokal, dan bisa diakses oleh banyak pengguna
- Untuk menambahkan remote repository server, gunakan command

```
git remote add origin [url]
```

## Mengirim perubahan ke server (Push)

- Untuk mengirim perubahan pada repositori lokal ke server, gunakan command

```
git push -u origin master
```

## Clone Repository

- git clone digunakan untuk mengambil salinan dari repositori Git dari server ke repositori lokal
- gunakan command ini untuk melakukan kloning ke repositori lokal

```
git clone [url]
```

## Berikut bukti pengerjaan-nya
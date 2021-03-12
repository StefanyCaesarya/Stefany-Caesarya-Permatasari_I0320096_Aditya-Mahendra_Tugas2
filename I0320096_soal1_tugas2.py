print("===== Menghitung Luas Persegi Panjang =====")
panjang = float(input("Memasukkan panjang"))
lebar = float(input("Memasukkan lebar"))
luas = panjang*lebar
print("Luas persegi panjang adalah", luas, "satuan")

print("===== Menghitung Luas Lingkaran =====")
phi = 3.14
jari_jari = float(input("Memasukan jari_jari"))
luas = jari_jari*jari_jari*phi
print("Luas lingkaran adalah", luas, "satuan")

print("===== Menghitung Luas Kubus =====")
sisi = float(input("Memasukka sisi"))
luas = 6*sisi*sisi
print("Luas Kubus adalah", luas, "satuan")

print("===== Menghitung Konversi Suhu Dari Celcius Ke Farenheit =====")
celcius = float(input("Memasukkan celcius"))
konversi = (((9/5)*celcius)+32)
print("Konversi Suhu Dari Celcius Ke Farenheit adalah", konversi, "derajat")

print("===== Menghitung Konversi Suhu Dari Reamur Ke Kelvin =====")
reamur = float(input("Memasukkan reamur"))
konversi = ((5/4)*reamur)+273
print("Konversi Suhu Dari Reamur Ke Kelvin adalah", konversi, "derajat")
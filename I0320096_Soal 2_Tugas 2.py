#Menampilkan informasi Program
print('\033[4m' + "IDENTITAS PRIBADI" + '\033[0m')

#Input Identitas Pribadi
nama_depan = "Stefany Caesarya"
nama_belakang = "Permatasari"
nama = nama_depan + nama_belakang
print("Nama : ",nama)
agama = "Islam"
print("Agama : ", agama)
jenis_kelamin = "Perempuan"
print("Jenis Kelamin : ", jenis_kelamin)
alamat_rumah = "Jalan Bentul VII"
alamat_norumah = int(5)
alamat_kodepos = int(60244)
alamat_kota = "Surabaya, Jawa Timur"
print("Alamat : ", alamat_rumah,"No.", alamat_norumah,"\n", alamat_kota,  alamat_kodepos)
hobi = "Bernyanyi dan Menonton"
print("Hobi : ", hobi)
bakat = "Bernyanyi"
print("Bakat : ", bakat)
tinggi_badan = float(171.0)
print("Tinggi Badan : ", tinggi_badan)
berat_badan = float(71.0)
print("Berat Badan : ", berat_badan)
uk_sepatu = float(41.0)
print("Ukuran Sepatu : ", uk_sepatu)
jurusan = "S-1 Teknik Industri"
angkatan = int(2020)
jalur_masuk = "Mandiri Prestasi"
ptn = "Universitas Sebelas Maret"
print("Pendidikan : ", "\n", "Prodi :", jurusan, "\n", "Angkatan : ", angkatan, "\n", "Jalur : ", jalur_masuk, "\n", "Universitas : ", ptn)

#Menampilkan data ke layar
print("Detail Umur")
#tanggal lahir
t = int(input("Tanggal lahir: "))
b = int(input("Bulan lahir: "))
th = int(input("Tahun lahir: "))
lahir = t + (b * 30) + (th * 365)

#tanggal sekarang
tgl = int(input("Tanggal : "))
bln = int(input("Bulan : "))
thn = int(input("Tahun : "))
skrg = tgl + (bln * 30) + (thn * 365)

#memulai proses kalkulasi
tahun = (skrg - lahir) / 365
bulan = ((skrg - lahir) % 365) / 30
hari = ((skrg - lahir) % 365) % 30
print("umur =",int(tahun),"tahun", int(bulan), "bulan", int(hari), "hari")
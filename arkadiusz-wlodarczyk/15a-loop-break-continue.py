# Di program pertama program akan berhenti berjalan
# dan menampilkan input ketika x kurang dari 0
# pada program kali ini kita menggunakan continue
# agar ketika input yang dimasukkan kurang dari 0 maka
# program akan kembali ke kondisi awal.
# masalahnya kita mengharapkan 3 kali input dari kode
# for i in range(3), jika hanya menggunakan continue
# kita hanya mendapatkan hasil input yang benar. Ini bisa
# jadi fatal ketika user salah input semua permintaan.
# Hasil yang akan didapat jadi 0
# jadi kita harus mengubahnya kembali
# ke while agar ketika user tidak memasukkan positive number
# program tidak akan menghitungnya dan terus loop sampai
# user memasukkan angka lebih dari 0

result = 0
i = 0

while i < 3 : 
    x = int(input("Masukkan angka positive: "))
    if (x > 0):
        result += x
    else :
        print("Silakan masukkan angka lebih dari 0")
        continue
    print ("jumlah yang anda masukkan saat ini adalah : ", result)
    i += 1
print("Total input anda adalah : ", result)

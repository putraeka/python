# apa itu list?
# cara membuat list?
# list dibuat dengan tanda [] setelah nama variable
# how to change the value of elements inside list
# how to print value
# how to print values at once
# why do you need list at all

names = ["Arkadiusz", "John", "Webley", "Jacob", "Whitney"]

number =[2, 7, 5, 30, 21]

buah = ["Anggur", "Mangga", "Semangka", "Apel", "Cherry"]

# urutan list dimulai dari 0 jika dihitung dari kiri (depan)
# jika dari belakang (kanan) maka dimulai dari -1

# cara mengganti value dari element dalam list

number[1] = 14
number[-1] = 45

print(number)

print(names)

# jika kita print variable dari list maka isi dari variable itu akan di print beserta []
# kalau ingin menampilkan isi list tanpa embel2 lain bisa menggunakan fungsi ini

for listbuah in buah:
    print(listbuah)

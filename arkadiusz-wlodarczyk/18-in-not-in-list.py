# in list
# not in list
# operation  in list

names = ["Lizzie", "Maria", "Cyntia", "Mila", "Corey"]

# mengetahui apakah value/element ada di dalam list

print ("Lizzie" in names)
print ("Debbie" in names)
# hasilnya akan menampilkan True or False

# menampilkan list juga bisa menggunakan if

if "Maria" in names :
    print("Hello Maria!")

# menampilkan value yang tidak terdapat dalam list

if "Dora" not in names :
    print("Just Lizzie")

# "not" bisa diletakkan sebelum element yang ingin dibandingkan kedalam list
# tapi lebih enak menggunakan "not in" secara langsung

if not "Qila" in names :
    print("There's no Qila here!")


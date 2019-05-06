# cara memasukkan functions dengan menggunakan (.)
# diakhir variabel diikuti tanda buku tutup kurung"()"
name = "john"
selo = "AYO"
when = "september"


print(name.upper())
print(selo.lower())
print(when.capitalize())

# user input secara default berupa strings
# ini berfungsi karena kita tidak tahu apa saja yang dimasukkan user kedalam form inputnya

#didi = input()
#keke = input()

a = int(input()) # it called CASTINGS, Change variable to
b = int(input()) # another variable
c = int(input("First number : "))
d = int(input("second number : "))
e = int(input("Your lucky number one: "))
f = int(input("Your lucky number two: "))

print("Sum of a + b is : " + str (a+b))
print("sum of c + d is : " + str (c+d))

# tanda + di fungsi print bisa digantikan dengan tanda ,
# jadi setelah tanda , tidak perlu menambahkan spasi lagi
# fungsi str juga bisa dihilangkan karena string pertama setelah
# tanda , selanjutnya tidak terkoneksi ke yang pertama

print("Sum of e + f is :", e+f)


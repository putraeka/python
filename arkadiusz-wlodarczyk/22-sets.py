# SETS sama seperti dictionary menggunakan curly bracket {}
# Element didalam SETS tidak bisa diganti, tapi bisa ditambahkan.
# Element harus unik
# Walaupun data yang dimasukkan kedalam sets tidak beraturan, tapi ketika memanggil variablenya SETS akan otomatis sorting dari yang element yang paling besar ke paling kecil.
# fungsi print(sorted(A)) akan menampilkan element dari yang paling kecil ke besar dan menghasilkan LIST
# Menambahkan element baru menggunakan :
# A.add(24)
# fungsi A.discard(-2) sama dengan fungsi del.rooms di DICT yaitu menghapus element dari SETS.

"""
SETS have bonus operations

| = Unions
& = Intersections
- = Difference
^ = XOR exclusive OR (removing Intersections from Unions)
"""

A = {40, -2, 20, 10}
B = {4, 7, 10, 20}

print (A|B)


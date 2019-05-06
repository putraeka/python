# Belajar loop lagi

"""
results = 0
i = 0

while i < 4 :
    nr = int(input("Please Input your number : "))
    results += nr
    i += 1

print("The results of adding number is : ", results)

"""

# Kondisi diatas bisa dipersingkat dengan menggunakan range

results = 0

for i in range(4):
    nr = int(input("Please Input your number : "))
    results += nr

print("The results of adding number is : ", results)

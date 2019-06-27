# Dibawah ada Nested List berisi Tuple
# Jika kita ingin memberikan setiap element dengan variable
# Kita bisa menggunakan loop for


guestList = [
                ('Arkadiusz', 29, 'man'),
                ('Jessica', 23, 'woman'),
                ('John', 32, 'man')
                
            ]             

for name, age, sex in guestList:
    print("Name: ", name)
    print("Age: ", age)
    print("Sex: ", sex)
    print()

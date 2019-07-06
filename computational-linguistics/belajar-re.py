import re

f = open('mobydick.txt', 'r')
lines = f.readlines()

for line in lines:
    # jika menggunakan re.match kita hanya menemukan kata yang berada
    # di awal line
    # tapi jika menggunakan re.search, jika akan menemukan 
    # kata didalam setiap line
    if re.search("Ahab", line):
        line = line.strip()
        print(line)
        
f.close()
# Demonstrate how to read file and
# parse it for particular patterns

def main():
    # read file
    f = open('yesno.txt', 'r')
    lines = f.readlines()
    f.close()
    
    # count for word Yes and No
    countYes = 0
    countNo = 0
    
    # look for patterns
    for line in lines:
        line = line.strip().upper()
        
        # jika menggunakan line.find kita hanya mendapatkan hasil
        # perbaris, misal dibaris yang sama ada 2 yes maka yang dihitung hanya satu
        # menggunakan line.find jika ada string "YES YES" dengan kondisi dibawah
        # maka line tersebut tidak dihitung
        if line.count("YES") != -1 and len(line) == 3:
            countYes += 1
        if line.count("NO") != -1 and len(line) == 2:
            countNo += 1
            
    # display result
    print("YES : ", countYes)
    print("NO :", countNo)
    
main()
# Membuat calculator berdasarkan input yang dimasukkan oleh user

menuOption = input("+ Add - Substract  * Multiply / divide : ")

first   = int (input("Input your first number : "))
second  = int (input("Input your second number: "))

if menuOption == '+' :
    print(first + second)
elif menuOption == '-' :
    print(first - second)
elif menuOption == '*' :
    print(first * second)
elif menuOption == '/' :
    if second  == 0 :
        print("Divided by zero, you can't do it!")
    else :
        print(first / second)
else :
    print("You must type one of the following character : +/-/* or /")



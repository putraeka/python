"""
break (leaves loop entirely)

continue (leave current iteration (repetition of loop), and CONTINUE)

"""

result = 0

for i in range(3):
    x = int(input("Please input positive number : "))
    if (x > 0):
        result += x
    else :
        print("That's not a positive number, program will closed")
        break
print("Your adding number is :", result)

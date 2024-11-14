number = int(input("Gimme a number: "))
if number == 10:
    print("number is 10")
elif number < 10:
    print("number is less than 10")
elif number >= 20:
    print("number is greater or equal to 20")
else:
    print("number is in between 11 and 19")

# id conditional statement executes only one line, it can be written like this
# number = int(input("Gimme a number: "))
# if number == 10: print("number is 10")

number = int(input("Gimme another number; "))
if number > 0 and number < 10:
    print("number is in between 1 and 9")
elif number >= 10 or number == 0:
    print("number is 10 or greater, or number is 0")

number1 = 4
number2 = 43
if number > number2:
    pass
else:
    print("no pass")

    

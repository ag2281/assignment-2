number = 5

account_balance = 110.54

print(number)
print(account_balance)


number = 55
number2 = number + 2
print("number 2 is" , number2)
print("number2 is " + str(number2))

print("Type of the variable 'number' is", type(number))
print("Type of the variable 'account_balance' is",type(account_balance))

# strings
first_name = "Gita"
last_name = "Bogati"

full_name = first_name + " " + last_name
print( full_name)

age = 21
person = "Frist name: {}.Last name: {}. Age: {}".formate(first_name, last_name, age)
print(person)

text = "ABC"
c1 = text[0]
c2 = text[1]
c3 = text[2]
print("Second char is " + c2)

print("Text lenght is", len(text))

text2 = "ABC"
if text == text2:
    print("Text are identical")
else:
    print("Text are not identical")

  # read text from Terminal
  #line = input("Enter a line of text: ")
  #print("You entered " + line)

 line = input("Enter a number: ")
 number = int(line)
 print("Number is", number)


number = 10
while number >= 0:
    print(number)
    number -= 1

for i in range(10):
    print("looping range(10):",i)

for number in range(5, 10):
    print("looping range(5, 10):", number)

for number in range(0,10,2):
    print("looping range(0, 10, 2):", number)

for c in "Basisc of programming with python":
    print(c)

names = ["Jani", "John", "Cherry", "Jack"]
for name in names:
    print(name)



# experiment the use of break and continue
print("Running a while loop with break")

while True:
    number = int(input("Enter a number (0 to exit): "))
    if number == 0:
        break
    elif number == 100:
         print("I don't like 100")
         continue
    
    print("You entered:", number)

print("Have a nice day!")


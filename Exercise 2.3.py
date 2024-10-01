'''
Declare a variable which is used to store bank account balance in euro (start balance of 2000 €). 
Print current balance into the console. Ask from user how many euro will be added to the balance. 
Then ask how many cents are added to the balance. Print the balance after user requested changes 
are made.
Example output:
'''

Bankbalance = 2000
print("Bank Balance is: ",Bankbalance)
# We are adding euros only
Euroadd = int(input("How many euros will be added to the balance?"))
# we are adding cents only
Centsadd = int(input("How many cents will be added to the balance?"))

Centchange = (Centsadd/100)

Newbalance = Bankbalance + Euroadd + Centchange
print(Newbalance)

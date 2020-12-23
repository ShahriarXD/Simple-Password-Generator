import random
uppercase_gens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_gens = uppercase_gens.lower()
digits_gens = "0123456789"
symbols_gens = ":()[]{},.;'>?</\\ #$%^&*@!"

upper, lower, digits, symbols = True,True,True,True

temp = ""
if upper:
    temp += uppercase_gens
if lower:
    temp += lowercase_gens
if digits:
    temp += digits_gens
if symbols:
    temp += symbols_gens

length = int(input("Please Enter The Lenghth of the Password: \n"))
amount = int(input("Please Enter The Ammount of the Password to be Generated: \n"))

for x in range(amount):   # loop runing the amount number of times
    password = "".join(random.sample(temp,length))
    print(password)



# What is random.sample?
# Ans : 
# import random 
# list1 = [1, 2, 3, 4, 5, 6]   
# print(random.sample(list1, 3))
# Output: [3, 1, 2]

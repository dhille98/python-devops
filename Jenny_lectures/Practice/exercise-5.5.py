# Pizza order codeing 

size = input("What size pizza you want(S/M/L)?")

bill = 0

if size == 'S' or size == 's':
    bill += 100
    print("your order Samll size pizza....")
elif size == 'M' or size == 'm':
    bill += 150 
    print("your order Medium size pizza....")
elif size == 'L' or size == 'l':
    bill += 250
    print("your order Large size pizza....")
else:
    print(f"Enter Valid size, your Enter {size}")

print(f"Your total pizza bill is: {bill}")

add_pepperoni = input("Do you want pepperoni(Y/N)?")

if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 's' or size == 'S':
        bill += 30 
    else:
        bill += 50
print(f"bill is {bill}")
extra_cheese = input("Do you want extra cheese(Y/N)?")

if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 50
    print("your seleted on extra cheese add coast on 50")

print(f"final bill is: {bill}")




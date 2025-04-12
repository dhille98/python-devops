# riding game 
height = int(input("Enter Your Height in feets: "))
if height >= 4:
    print("you can Ride")
    age = int(input("Enter your age: "))
    if age <= 12:
        print(f"your age is {age} pls pay the amount Rs 250") 
    elif age <= 18:
        print(f"your age is {age} pls pay the amount Rs 350")     
    else:
        print(f"your age is {age} pls pay the amount Rs 500")
else:
    print("can't ride")
print("Thank You")
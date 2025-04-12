# find the leap year not 

year = int(input("Which year you want to check ?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is non leap year")
    else: 
        print(f"{year} is leap year")
else:
    print(f"{year} is non leap year")

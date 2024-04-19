telugu =int(input("enter your telugu marks: "))
english =int(input("enter your english marks: "))
hindi=int(input("enter your hindi marks: "))
mathes =int(input("enter your mathes marks: "))
sceince =int(input("enter your sceince marks: "))
scocial =int(input("enter your scocial marks: "))

average = (telugu+english+hindi+mathes+sceince+sceince) // 6

print(average)

if average >= 90 and average <= 100:
    print("A1")
elif average >= 80 and average <= 90:
    print("A2")
elif average >= 70 and average <= 80:
    print("B1")
elif average >= 60 and average <= 70:
    print("B2")
elif average >= 50 and average <= 60:
    print("C1")
elif average >= 40 and average <= 50:
    print("C2")
elif average >= 35 and average <= 40:
    print("D")
elif average <= 35:
    print("F")
else:
    print(" enter correct marks ")


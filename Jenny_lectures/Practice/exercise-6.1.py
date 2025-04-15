# who will play the bill

import random

names = input("Enter your friends names by comma:")

name_list = names.split(",")

print(name_list)
# length=len(names_list)
# random_choice = randint(0, length-1)
# print(name_list[random_choice])
pay_person = random.choice(name_list)

# bill_person = print(pay_person)

print(f"bill pay persion {pay_person}")
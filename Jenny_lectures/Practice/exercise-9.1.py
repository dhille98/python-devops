# find large number in the list

number = input("Enter the number with space: ")

number_list = number.split()

print(number_list)

count = 0

for number in number_list:
    count += 1

print(count)

for i in range(count):
    number_list[i] = int(number_list[i])

print(number_list)

maimum_number = max(number_list)

print(f"maxmum of list is: {maimum_number}")
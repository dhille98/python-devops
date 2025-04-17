
import random
print("Welcome to password?")

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

number = ["0", "1", "2" ,"3", "4", "5", "6", "7", "8", "9"]

symbloes = ["@", "#", "$", "&", "!"]

number_letters = int(input("How many letters would you like in your password? "))

number_symboles = int(input("how many symboles would you like(1-5) ?"))

n_numbers = int(input("how many numbers would you like ?"))


password_list = []

for i in range(1, number_letters+1):
    char = random.choice(letter)
    password_list += char
for i in range(1,number_symboles+1):
    char = random.choice(symbloes)
    password_list += char
for i in range(1, n_numbers):
    char = random.choice(number)
    password_list += char
print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char
print(password)
# password generator ! 

# How many letters would you like in your password?
# how many symboles would you like ?
# how many numbers would you like ?
 
import random
print("Welcome to password?")

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

number = ["0", "1", "2" ,"3", "4", "5", "6", "7", "8", "9"]

symbloes = ["@", "#", "$", "&", "!"]

number_letters = int(input("How many letters would you like in your password? "))

number_symboles = int(input("how many symboles would you like(1-5) ?"))

n_numbers = int(input("how many numbers would you like ?"))

password = ""
for i in range(1,number_letters+1):
    char = random.choice(letter)
    password += char
for i in range(1, number_symboles+1):
    sym = random.choice(symbloes)
    password += sym
for i in range(1, number_letters+1):
    num = random.choice(number)
    password += num
print(password)

import random
secret_num = random.randint(1 , 100)

attempts = 0

print("Number between 1 - 100, guess the number")

while True:
    guess_number = int(input("Enter Number:"))

    attempts += 1

    if secret_num > guess_number:
        print("Too low! Try again.")
    elif secret_num < guess_number:
        print("Too high! Try again.")
    else:
        print(f'you enter the correct number no.of attempts is {attempts}')
        break

    


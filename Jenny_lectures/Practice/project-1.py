# Rock Paper scissors 
import random

user_choice = int(input("Enter your Choice: type 1 for paper, 2 for scissers."))
if user_choice >= 3 or user_choice < 3:
    print("you entered invalid number, you lose.")
else:
    computer_choice = random.randint(0,2)
    print(f"computer Chose: {computer_choice}")
    # write a 6 conditions 
    if computer_choice == user_choice:
        print("It's a draw")
    elif computer_choice == 0 and user_choice == 2:
        print("Your Lose the Game")
    elif user_choice == 0 and computer_choice == 2:
        print("Your Win the Game")
    elif computer_choice > user_choice:
        print("Your Lose the Game")
    elif user_choice > computer_choice:
        print("You will win the Game")



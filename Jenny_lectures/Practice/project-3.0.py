# Hangman Game 
import random
words = ["apple", "plane", "python","coding", "light",  ]

chosen_word = random.choice(words)
lives = 6
# print(chosen_word)

display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)



game_over = False
while not game_over:
    guess_letter = input("Guess The letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess_letter == letter:
            display[position] = guess_letter
    print(display)

    if guess_letter not in chosen_word:
        lives -= 1
        print("Remaing lives are", lives)
        if lives == 0:
            game_over = True
            print("You are Lose!!")
    if '_' not in display:
        game_over = True
        print("Your are win game !!")
        print("The Word is:",chosen_word )


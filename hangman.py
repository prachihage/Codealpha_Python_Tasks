import random

words = ["apple", "mango", "grape", "table", "chair"]

word = random.choice(words)

guessed = []
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("You Won!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        chances -= 1
        print("Wrong Guess")
        print("Chances Left:", chances)

if chances == 0:
    print("Game Over")
    print("Word was:", word)
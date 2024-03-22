import random

print("Welcome to the number guessing name !")
print("------------------------------------")
random_number = random.randint(1, 101)
print("Iam thinking of a number between 1 and 100")
difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    hints = 10
elif difficulty == 'hard':
    hints = 5

print(f"You have {hints} attempts to guess the number")

game_finished = False
i = hints
while not game_finished:
    guess = int(input("Make a guess: "))
    if guess == random_number:
        game_finished = True
        print("------------------------------------")
        print(f"HURRAY ! you guessed the correct number")
        print("------------------------------------")
    elif guess > random_number:
        print("too high")
        print(f"You have {i - 1} guesses remaining")
    elif guess < random_number:
        print("too low")
        print(f"You have {i - 1} guesses remaining")
    i -= 1
    if i == 0:
        print("------------------------------------")
        print("you loose")
        print("------------------------------------")
        print(random_number, " is the number")
        game_finished = True

#Guessing number game

import random
import time


print("Welcome to guessing game, I am going to pick a number between 1 and 50")
time.sleep(1)
print("Picking a number....")
time.sleep(1)
guess_number = int(input("Guess a number :"))
correct_number = random.randint(1, 50)
guess_count = 1



while guess_number != correct_number:
    guess_count += 1
    if guess_number < correct_number:
        guess_number = int(input("Wrong you need to guess higher. What is your guess?: "))
    else:
        guess_number = int(input("Wrong you need to guess lower. What is your guess?: "))

print(f"Congrats, you've guessed the right answer which is {correct_number} and you have guessed it in {guess_count} attempts.")


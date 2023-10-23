# Predicting fortune based on lucky number

import random

rand_numb = random.randint(1, 9)

if rand_numb < 4:
    print(f"Your are going to have a great day! and your lucky number is {rand_numb}")
else:
    print(f"You are in for a fab time, checkout your lucky charming number, which is {rand_numb}")



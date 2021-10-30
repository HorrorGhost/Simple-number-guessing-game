import time
import random

correct_guess = random.randint(0,5+1)
guess_limit = 3
guess_count = 0

print("You will get 3 chances to guess the number")
time.sleep(1)

print("You have to guess a number between 1 to 5")
time.sleep(1)

while guess_count < guess_limit:
    
    guess = int(input("Enter a number: "))
    guess_count += 1
    
    if guess == correct_guess:
        print("You won!")
        break
    print("Wrong!")
else:
    print("You lost!")

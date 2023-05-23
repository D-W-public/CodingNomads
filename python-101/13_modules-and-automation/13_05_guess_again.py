# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num = random.randint(1,10)

guess = None

count = 3

while count > 0:
    count -= 1
    while guess != num:
        guess = int(input("guess a number between 1 and 10: "))
        
        if guess == num:
            print("Congratulations you won!")
        
        else:
            print(f"Nope,you have {count} more tries ")
            break
    if count == 0:
        print("Game Over!")

import random

#determine unser and computer input

correct_input = None
computer_input = random.randint(0, 2)


while correct_input == None:
    try:
        user_input = int(input("Please enter a number between 0 and 2:\n"))
    
        if user_input in range(3):
            correct_input = True
            break
        elif user_input not in range(3):
            print("Number not in range.")
    except ValueError:
        print("Invalid input")


def get_hand(hand):
    """Returns hands."""
    if hand == 0:
        h = "scissors"
    elif hand == 1:
        h = "rock"
    else:
        h = "paper"
    return h



print(get_hand(user_input))
print(get_hand(computer_input))


def det_winner(hand1, hand2):
    """determins winner of the game"""
    if hand2 > hand1:
        


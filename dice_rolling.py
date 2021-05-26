import random


def roll_the_dice(min_dice,max_dice):
    user_choice = 'y'
    
    while user_choice == 'y':
        print("Rolling the dice now", "\n")
        print("Your number is: " + str(random.randint(min_dice,max_dice)) + "\n")
        user_choice = input("Wanna roll the dice again? (y/n): ")






roll_the_dice(1,6)
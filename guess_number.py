import random

def guess_number():
    cnumber = random.randint(1,20)
    gnumber = int(input("Can you guess the number? Try any integral number: "))
    while gnumber != cnumber:
        if gnumber > cnumber:
            print("Your guess, ", gnumber, ", is too high!")
            gnumber = int(input("Try again: "))

        else:
            print("Your guess, ", gnumber, ", is too low!")
            gnumber = int(input("Try again: "))
    print("Hooray!!!! Congratulations, you guessed the number correctly!")


guess_number()
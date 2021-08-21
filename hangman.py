import random

words_pool = ('ant', 'baboon', 'camel', 'deer', 'eagle', 'frog', 'goat', 'hippopotamus', 'iguana', 'jaguar', 'kangaroo', 'lion', 'monkey', 
'narwhal', 'owl', 'parrot', 'quail', 'rabbit', 'shark', 'tiger', 'umbrellabird', 'vulture', 'whale', 'yak', 'zebra')

def position(pos, word, letter):
    for i,x in enumerate(word):
        if x == letter:
            pos = pos[:i] + letter + pos[i+1:]
    return pos

def check_guess(pos, letter, word):
    if letter in (word):
        return position(pos, word, letter = letter)
    else:
        return []

def concat_guess(guess, nlist = []):
    if guess not in nlist:
        nlist.append(guess)
    else:
        pass
    return nlist

def main_play():
    print('\n')
    print("Shall we play hangman?")

    word = random.choice(words_pool)
    positions = '_' * len(word)
    total_chance = len(word) * 2

    print('\n')
    print("You've got to guess a " + str(len(word)) + " letter word." + "\n" + positions)
    print("HINT: it's an animal")

    while (positions != word) and (total_chance > 0):
        print("Number of chances: " + str(total_chance))
    
        guess_letter = input("What's your letter guess?: ")
        concat = concat_guess(guess_letter)
        
        bool_check = check_guess(positions, guess_letter, word)

        if len(bool_check) > 1:
            positions = bool_check
            print(positions)
        else:
            print("Letters you already played: ")
            print(concat)
            total_chance -= 1
        

    if positions == word:
        print('\n')
        print("Congratulations!!!")
        print('\n')
        play_again = input("Do you want to play again? [y/n]: ")
        if play_again == 'y':
            main_play()
        else:
            print("Thanks for playing, see you next time!")
    else:
        print("Bad luck! The word you were trying to guess was: " + word.upper())

main_play()



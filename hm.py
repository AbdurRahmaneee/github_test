import numpy as np
import random
x = 5 + 5
y = 34
f = 4
def hangman():
    word = random.choice(['jake','chill','cat','lion','bla','tata'])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade=''

    while len(word)>0:
        main = ''
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main+letter
            else:
                main = main + '_'+''
        if main==word:
            print(main)
            print('you win!')
            break
        print('guess the main word', main)
        guess = input()
        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print('enter a valid character')
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns==9:
                print('9 turns left')
                print(' --------  ')
            if turns == 8:
                print('8 tunrs left')
                print(' --------')
                print('     O     ')
            if turns == 7:
                print('7 turns left')
                print(' -------- ')
                print('     O    ')
                print('     |    ')
            if turns==6:
                print('6 turns left')
                print(' -------- ')
                print('     O    ')
                print('     |    ')
                print('     /    ')
            if turns==5:
                print('5 turns left')
                print(' -------- ')
                print('     O    ')
                print('     |    ')
                print('    / \    ')
            if turns == 4:
                print('4 turns left')
                print(' -------- ')
                print('   \ O    ')
                print('     |    ')
                print('    / \    ')
            if turns == 3:
                print('3 turns left')
                print(' -------- ')
                print('   \ O /    ')
                print('     |    ')
                print('    / \    ')
            if turns==2:
                print('2 turns left')
                print(' -------- ')
                print('   \ O /|   ')
                print('     |    ')
                print('    / \    ')
            if turns == 1:
                print('1 turns left')
                print(' -------- ')
                print('   \ O_|/   ')
                print('     |    ')
                print('    / \    ')
            if turns == 0:
                print('0 turns left')
                print('you lose... he died')
                print(' -------- ')
                print('     O_|   ')
                print('    /|\    ')
                print('    / \    ')
                break



name = input("enter youur name: ")
print('welcome', name)
print("------------")
print("try to guess the name in less than 10 attempts")
hangman()

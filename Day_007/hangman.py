#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random
import os
from hangman_art import logo, stages
from hangman_words import word_list


hangman = []
check_alpha = ""
lives = 6
word = random.choice(word_list)    # 임의 단어 선정(랜덤)
for i in range(len(word)):
    hangman += "_"

print(logo)
print("[Game Start] hangman")
while lives:
    alpha = input("please input alpha : ")

    if check_alpha.count(alpha):
        print("already input alpha")
        continue

    if word.count(alpha):
        for n, i in enumerate(word):
            if i is alpha:
                hangman[n] = alpha
    else:
        lives -= 1

    os.system('clear')
    print(f"lives : {lives}")
    print(('').join(hangman))
    print(stages[lives])

    if not hangman.count("_"):
        print("Game Clear!!")
        break
    check_alpha += alpha

if not lives:
    print("Game Over")
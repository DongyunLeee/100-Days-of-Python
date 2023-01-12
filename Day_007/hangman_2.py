#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

hangman = []
word = random.choice(word_list)    # 임의 단어 선정(랜덤)
for i in range(len(word)):
    hangman.append("_")

count = 0
while count < 7:
    alpha = input("please alpha : ")
    if word.count(alpha):
        for n, i in enumerate(word):
            if i is alpha:
                hangman[n] = alpha
    else:
        count += 1

    print(f"life count : {count} {('').join(hangman)}")

    if not hangman.count("_"):
        print("Game Clear!!")
        break

    if count == 7:
        print("Game Over")



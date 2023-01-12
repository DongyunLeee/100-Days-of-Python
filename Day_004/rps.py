import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rps = [rock, paper, scissors]
my_rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(rps[my_rps])

com_rps = random.randint(0, 2)
print("Computer chose:\n")
print(rps[com_rps])

if my_rps ==0 and com_rps ==2:
    print("You win!")
elif my_rps == 2 and com_rps == 0:
    print("You lose")
elif my_rps == com_rps:
    print("you draw")
elif my_rps > com_rps:
    print("You win!")
else:
    print("You lose")
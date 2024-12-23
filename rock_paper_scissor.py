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
---'   _____)____
          _______)
          ________)
         ________)
---.___________)
'''

scissors = '''
    _______
---'   ____)____
          ________)
       ____________)
      (____)
---.__(___)
'''

import random
game = [rock, paper, scissors]
flag = True
while flag :
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
    print(game[user])
    print("\n")
    print("Computer chose :\n")
    r = random.randint(0,2)
    print(game[r])
    print("\n")
    if user == 0 and r == 2:
        print("Yay! You won.")
    elif user == 2 and r == 0:
        print("You lose.")
    elif user > r:
        print("Yay! You won.")
    elif user == r:
        print("It's a draw.")
    else:
        print("You lose.")
    go_again = input("Would you like to play again ? Type 1 for Yes and 0 for No ")
    if go_again == 0:
        flag = False
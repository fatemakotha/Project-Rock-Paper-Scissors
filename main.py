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

playing_images = [rock, paper, scissors]#rock=0th index, paper=1st index and scissors=2nd index

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(playing_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(playing_images[computer_choice])


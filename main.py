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
rpc = [rock, paper, scissors]
print(rpc)

agent_input = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

if agent_input == 0:
  random_decision = random_decision.choice(rpc)
  
  print(f"Computer chose {random_decision}")




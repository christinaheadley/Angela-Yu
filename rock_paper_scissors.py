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
options = ["rock", "paper", "scissors"]
print("Computer playing...")
computer_pick = random.choice(options)
player_pick = input(f"Please select {options[0]}, {options[1]}, or {options[2]}. ") #or enter 0 for rock...
print("You played " + player_pick)
print("The computer played " +computer_pick)

if computer_pick == player_pick:
  print("It's a tie!")
elif computer_pick == "rock":
  if player_pick == "scissors":
    print("Rock beats scissors, you lose this round 😛")
  elif player_pick == "paper":
    print("Paper beats rock, you win this round!")
  else:
    print("Invalid response. You lose.")
elif computer_pick == "scissors":
  if player_pick == "paper":
    print("Scissors beats paper, you lose this round 😛")
  elif player_pick == "rock":
    print("Rock beats scissors, you win this round!")
  else:
    print("Invalid response. You lose.")  
elif computer_pick == "paper":
  if player_pick == "scissors":
    print("Paper beats scissors, you lose this round 😛")
  elif player_pick == "rock":
    print("Paper beats rock, you win this round!")
  else:
    print("Invalid response. You lose.")

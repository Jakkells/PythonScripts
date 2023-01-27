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

print("")
print("Welcome to rock paper scissors!")
print("-------------------------------------\n")

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

choicesUser = ["Rock", "Paper", "Scissors"]
userChose = choicesUser[userChoice]
print("")
print(f"User Chose {userChose}:\n")

if userChoice == 0:
    print(rock)

if userChoice == 1:
    print(paper)

if userChoice == 2:
    print(scissors)

computerChoice = random.randint(0, 2)
choicesComputer = ["Rock", "Paper", "Scissors"]
computerChose = choicesComputer[computerChoice]
print("")
print(f"Computer Chose {computerChose}:\n")

if computerChoice == 0:
    print(rock)

if computerChoice == 1:
    print(paper)

if computerChoice == 2:
    print(scissors)


if userChoice >= 3 or userChoice < 0:
  print("You typed an invalid number, you lose!")
elif userChoice == 0 and computerChoice == 2:
  print("You win!")
elif computerChoice == 0 and userChoice == 2:
  print("You lose")
elif computerChoice > userChoice:
  print("You lose")
elif userChoice > computerChoice:
  print("You win!")
elif computerChoice == userChoice:
  print("It's a draw")


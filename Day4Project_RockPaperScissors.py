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
#print (paper)
# Optimal Solution
userinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computerchoice=random.randint(0, 2)

symbols = [rock, paper, scissors]
if userinput >= 3 or userinput < 0:
  print("You typed an invalid number, you lose.")
else:
  print(f"Your choice: \n {symbols[userinput]}")  
  print(f"Computer chose: \n {symbols[computerchoice]}")
    
  if userinput == 0 and computerchoice == 2:
    print("You win!!")
  elif computerchoice == 0 and userinput == 2:
    print("You Lose")
  elif computerchoice > userinput:
    print("You Lose")
  elif userinput > computerchoice:
    print("You win!!")
  elif computerchoice == userinput:
    print("It's a draw !!")

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
import random

person_choice = input("What do you choose? 0 for Rock, 1 for paper, or 2 for scissors? ")
int_person_choice = int(person_choice)

#Display person's picture

if int_person_choice == 0:
  print(rock)
elif int_person_choice == 1:
  print(paper)
elif int_person_choice == 2:
  print(scissors)

# Determine Computer's Choice

print("Computer chose: ")

computer_options = [0, 1, 2]

computer_choice = (random.choice(computer_options))
# print(computer_choice)

# Display computer's picture

if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

# Determine Outcome

if int_person_choice == 0:
  
  if computer_choice == 0:
    print("It's a draw. Try again.")
  elif computer_choice == 1:
    print("You lose. Try again!")
  else:
    print("You win! Congratulations!")

elif int_person_choice == 1:
  
  if computer_choice == 0:
    print("You win! Congratulations!")
  elif computer_choice == 1:
    print("It's a draw. Try again!")
  else:
    print("You lose. Try again!")
  
elif int_person_choice == 2:
 
  if computer_choice == 0:
    print("You lose. Try again!")
  elif computer_choice == 1:
    print("You win! Congratulations!")
  else:
    print("It's a draw. Try again!")















# # result 
# if pc_rock < int_choice:
#   print("You lose.")

# pc_rock = options[0]
# print(pc_rock)
# pc_paper = options[1]
# pc_scissors = options[2]
# # int_pc_rock = int(pc_rock)
# print(int_pc_rock)


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
sign_image=(rock,paper,scissors)
print ("Welcome to the game of Rock, Paper, Scissors!\n")
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if (user_choice>=0 and user_choice<=2):
    print("You choose:\n" + sign_image[user_choice])
computer_choice=random.randint(0,2)
print("Computer chose:\n" + sign_image[computer_choice])

if (user_choice <0 or user_choice >=3):
    print("You typed an invalid option. You lose!")
elif(user_choice== 0 and computer_choice==2):
    print("You win!")
elif (user_choice < computer_choice):
    print("You lose!")
elif (computer_choice == user_choice):
    print("It's a draw!")
elif (computer_choice == 0 and user_choice == 2):
    print("You lose!")
elif (computer_choice < user_choice):
    print("You win!")



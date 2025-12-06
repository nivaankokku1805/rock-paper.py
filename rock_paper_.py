import random

user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

if user_choice == computer_choice:
   print(f"Both chose {user_choice}. It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "scissors" and computer_choice == "paper") or \
    (user_choice == "paper" and computer_choice == "rock"):
   print(f"You win! {user_choice.capitalize()} beats {computer_choice}.")
else:
   print(f"You lose! {computer_choice.capitalize()} beats {user_choice}.")
   
while True:
   user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
   computer_choice = random.choice(options)
   print(f"You chose {user_choice}, computer chose {computer_choice}.")
   if user_choice == computer_choice:
       print("It's a tie!")
   elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
       print("You win!")
   else:
       print("You lose!")
   play_again = input("Play again? (y/n): ").lower()
   if play_again != 'y':
       print("Thanks for playing!")
       break


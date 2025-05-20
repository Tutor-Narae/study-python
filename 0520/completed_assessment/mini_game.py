# new features
# elif command == play
import random

class Mini_game():
  def play(self):
    is_win = False
    is_draw = True

    print("Welcome to the mini game!")

    while is_draw:
      choices = ["rock", "scissors", "paper"]

      # computer_choice = random.choice(choices)
      computer_choice = "rock"
      user_choice = input("choose one of rock, scissors, paper:")

      print(f"You: {user_choice}, Enemy: {computer_choice}")

      if user_choice in choices:
        if user_choice == computer_choice:
          print("You've got the same one with him. Do you want to play again?")

          command = input("(yes/no) >")
          if command.lower() == "yes":
            is_draw = True
          else:
            is_draw = False
            is_win = False

        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
          print("Congratulations! You've won the mini game!!")
          is_draw = False
          is_win = True

        elif (user_choice == "rock" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "rock"):
          print("Ooops, you lost the game.")
          print("That's the end of the game.")
          is_draw = False
          is_win = False

      else:
        print("Select again, please")

    return is_win
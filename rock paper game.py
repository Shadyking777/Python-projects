import random

def rps_game():
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("rock / paper / scissors (or exit): ").lower()
        if user == "exit":
            break

        computer = random.choice(choices)
        print("Computer:", computer)

        if user == computer:
            print("Tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win 🎉")
        else:
            print("You lose 😢")

rps_game()

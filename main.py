
# Basic Rock Paper Scissors Game
# Name: Francesca Hoh
# Date: 2/15/26

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

def get_user_choice():
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	console.print(f"Options: {choices}")
	console.print(num_to_choice)
	user_choice = console.input("Chose one")

	while True:
		if user_choice in num_to_choice:
			return num_to_choice[user_choice]
		else:
			user_choice = console.input("")

 


def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	computer_choice = random.choice(choices)
	return computer_choice




def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	if user_choice == computer_choice:
		return "tie"
	elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
		return "user"
	else:
		return "computer"


def print_round_result(user_choice, computer_choice, winner):
	"""Print the choices and the winner of the round using rich colors."""
	console.print("You chose: ", user_choice)
	console.print("Computer chose: ", computer_choice)
	if winner == "user":
		console.print("You won the round")
	elif winner == "computer":
		console.print("Computer won this round")
	else:
		console.print("It's a tie")


def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		user_choice = get_user_choice()
		computer_choice = get_computer_choice()
		winner = determine_winner(user_choice, computer_choice)
		print_round_result(user_choice, computer_choice, winner)
		if winner == "user":
			user_score += 1
		elif winner == "computer":
			computer_score += 1

	print("Player Score: ",  user_score, "Computer Score: ", computer_score)
	if user_score > computer_score:
		console.print("[bold green]Congratulations, you win the game![/bold green]")

if __name__ == "__main__":
	main()


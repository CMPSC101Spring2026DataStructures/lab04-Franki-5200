
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

# Create a Console object for rich output
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
	print(f"Options: {choices}")
	print(num_to_choice)
	user_choice = console.input("Chose one")

	while True:
         if user_choice == "1" or user_choice == "2" or user_choice == "3":
		    return user_choice
		else:
            user_choice = console.input("")

 


def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	computer_choice = random.choice(choices)
	return computer_choice



# TODO: Implement this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	pass

# TODO: Implement this function to print the round result with color.
def print_round_result(user_choice, computer_choice, winner):
	"""Print the choices and the winner of the round using rich colors."""
	pass

# TODO: Implement the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		# TODO: Get user and computer choices
		get_user_choice()
		get_computer_choice()
		# TODO: Determine winner
		# TODO: Print round result
		# TODO: Update scores
		pass
	# TODO: Print final scores and announce the overall winner
	pass

if __name__ == "__main__":
	main()
	if user_score > computer_score:

		console.print("[bold green]Congratulations, you win the game![/bold green]")

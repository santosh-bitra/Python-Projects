# Rock Paper and Scissors Game

import random

rock = '''🗿'''
paper = '''📜'''
scissors = '''✂'''
images = [rock, paper, scissors]

List = ["rock", "paper", "scissors"]

player_chooses = input("What do you choose ? ").lower()

computer_chooses = random.choice(List)


if player_chooses == List[0] and computer_chooses == List[2]:
    print(f"The player choose {images[0]} \nbut the computer choose {images[2]} \n You Win")
elif player_chooses == List[1] and computer_chooses == List[0]:
    print(f"The player choose {images[1]} \nwhile the computer choose {images[0]} \n You Win")
elif player_chooses == List[2] and computer_chooses == List[1]:
    print(f"The player choose {images[2]} \nbut the computer choose {images[1]} \n You Win")
elif player_chooses == computer_chooses:
    print("Draw")
else:
    print("You Lose")


user_name=input("Hi! What's your name? ")
print(f"Welcome to my game of RPS, " + user_name + "!\n")
#player2=input("Please choose rock, paper, or scissors. \n")

import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"

# player1 = choose_rps()
# player2 = choose_rps()

def rps(player1, player2):
  """
  input: the strings player1 and player2
  output: winner of the game rock, paper, scissors
  """
  if player1 == player2:
    print("It's a tie!")
  elif player1 == "rock":
    if player2 == "scissors":
      print("Player 1 won!")
    else:
      print("Player 2 won!")
  elif player1 == "paper":
    if player2 == "rock":
      print("Player 1 won!")
    else:
      print("Player 2 won!")
  elif player1 == "scissors":
    if player2 == "paper":
      print("Player 1 won!")
    else:
      print("Player 2 won!")

# print("Player 1 chose " + player1 + ".")
# print("Player 2 chose " + player2 + ".\n")

# rps(player1,player2)

play = random.randint(0,1)
while play:
  if play == True:
    player1 = choose_rps()
    player2 = choose_rps()
    winner = rps(player1,player2)
    # print(winner)
    print("Player 1 chose " + player1 + ".")
    print("Player 2 chose " + player2 + ".\n")
    print(winner)
  else:
    print("Thank you for playing!")

# rps(player1,player2)
# player1 = choose_rps()
# print(player1)
# player2 = choose_rps()
# rps(player1,player2)
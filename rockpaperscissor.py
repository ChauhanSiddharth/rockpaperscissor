import random
player1 = ""
player2 = ""
input_1 = "rock"
input_2 = "paper"
input_3 = "scissors"
computer_list = ["rock","paper","scissors"]

y = 0

print("Rules:\
		\nRock beats scissors \
		\nScissors beats paper\
		\nPaper beats rock \nLets see Who win GO GO GO\n")

print("Computer selecting from rock,paper or scissors...")
player1 = random.choice(computer_list)
print("Computer Selected")
print("\n")

while y == 0:
	player2 = input("Player 2: Select \nrock \npaper \nscissors = ")
	if player2 == input_1:
		y = 1
	elif player2 == input_2:
		y = 1
	elif player2 == input_3:
		y = 1

if (player1 == player2):
	print("Draw!")
	print("Computer Selected " + player1)
elif(player1 == input_1 and player2 == input_3) or (player1 == input_2 and player2 == input_1) or (player1 == input_3 and player2 == input_2):
	print("Computer Wins!")
	print("Computer Selected " + player1)
elif(player1 == input_2 and player2 == input_3) or (player1 == input_3 and player2 == input_1) or (player1 == input_1 and player2 == input_2):
	print("Player 2 Wins!")
	print("Computer Selected " + player1)
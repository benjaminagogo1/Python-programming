import random
import sys

playerChoice = input("Enter...\n1. Rock\n2. Paper\n3. Scissor\n")


player = int(playerChoice)

if player < 1 or player > 3:
    print("You must choose 1, 2 or 3.")
    sys.exit()

computerChoice = random.choice("123")

computer = int(computerChoice)

print("You chose " + playerChoice + ".")
print("python chose " + computerChoice + ".")

print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😄 Tie game!")
else:
    print("python win!")
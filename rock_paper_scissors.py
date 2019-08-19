import random

print("...rock...\n...paper...\n...scissors...\n")

print("Enter Player 1's choice: ")
p1 = str(input())

p2 = random.choice(["rock", "paper", "scissors"])

# Alternative way to get computer guess
#computer_num = random.randint(0, 2)
#num_to_choice = {
#    0: "rock",
#    1: "paper",
#    2: "scissors"
#}

# Maps the random int generated to rock, paper or scissors
#p2 = num_to_choice[computer_num]


message = None
print(f"Computer picks {p2}")

if p1 == p2:
    message = "DRAW"
# p1 wins
elif (p1 == "rock" and p2 != "paper") or (p1 == "paper" and p2 != "scissors") or (p1 == "scissors" and p2 != "rock"):
    message = "Player 1 wins"
# p2 wins
elif (p2 == "rock" and p1 != "paper") or (p2 == "paper" and p1 != "scissors") or (p2 == "scissors" and p1 != "rock"):
    message = "Computer wins"
else:
    message = "Incorrect input"

print(f"\n{message}")

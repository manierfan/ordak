import random
a = ["rock", "paper", "scissors"]
rps = input ("select [rock or paper or scissors]")
b = random.choice(a)
print (f"player choice {rps}, computer choice {b}")
if rps == b:
    print ("draw")
if rps == "rock":
    if b =="paper":
        print ("computer win")
if rps == "paper":
    if b == "rock":
        print("player win")
if rps == "paper":
    if b == "scissors":
        print ("computer win")
if rps == "scissors":
    if b == "paper":
        print ("player win")
if rps == "rock":
    if b == "scissors":
        print ("player win")
if rps == "scissors":
    if b == "rock":
        print ("computer win")



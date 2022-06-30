import random
ba_ki = input("You want to play with computer [1] or player 2 [2] ?")
tedad = int(input ("How many times you want to play ?"))
entkhab = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
player1_score = 0
player2_score = 0
if ba_ki == "1": 
    while tedad != 0 :
        computer = random.choice(entkhab)
        player =input("select rock[1] or paper[2] or scissors[3]:")
        if player=="1":
            p3 ="rock"
        if  player=="2":
            p3 ="paper"
        if  player=="3":
            p3 = "scissors"                    
        print (f"player choise {p3} and computer choice {computer}")
        if player == computer:
            print ("draw")
        if player == "1" and computer == "scissors":
                print ("player win")
                player_score = player_score + 1
        if player == "1" and computer =="paper":
                print ("computer win")
                computer_score = computer_score + 1
        if player == "2" and computer == "rock":
                print("player win")
                player_score = player_score + 1
        if player == "2" and computer == "scissors":
                print ("computer win")
                computer_score = computer_score + 1
        if player == "3" and computer == "paper":
                print ("player win")
                player_score = player_score + 1
        if player == "3" and computer == "rock":
                print ("computer win")
                computer_score = computer_score + 1
        print (f"player {player_score} computer {computer_score}")
        print("--------------------------------------------------------------------------------------------------------------------------")                
        tedad -= 1       
if ba_ki ==  "2":
    name_1 = input ("enter your name (player 1):") 
    name_2 = input ("enter your name (player 2):")
    while tedad != 0:
        player_1 = input("select rock[1] or paper[2] or scissors[3]:")
        player_2 = input("select rock[1] or paper[2] or scissors[3]:")
        if player_1=="1":
            p1 ="rock"
        elif  player_1=="2":
            p1 ="paper"
        elif  player_1=="3":
            p1 = "scissors"
        else :
            p1 ="wrong"
        if player_2=="1":
            p2 ="rock"
        elif  player_2=="2":
            p2 ="paper"
        elif  player_2=="3":
            p2 = "scissors"
        else :
            p2 ="wrong"
        print (f"{name_1} choice {p1} and {name_2} choice {p2}")
        if player_1 == player_2:
            print ("draw")
        if player_1 == "1" and player_2 == "2":
                print(f"{name_2} win")
                player2_score = player2_score + 1
        if player_1 == "1" and player_2 == "3":
                print (f"{name_1} win")
                player1_score = player1_score + 1
        if player_1 == "3" and player_2 == "1":
                print(f"{name_2} win")
                player2_score = player2_score + 1
        if player_1 == "3" and player_2 == "2":
                print (f"{name_1} win")
                player1_score = player1_score + 1
        if player_1 == "2" and player_2 == "3":
                print(f"{name_2} win")
                player2_score = player2_score + 1
        if player_1 == "2" and player_2 == "1":
                print (f"{name_1} win")
                player1_score = player1_score + 1
        print (f"{name_1} [{player1_score}] {name_2} [{player2_score}]")
        print("------------------------------------------------------------------------------------------------------------------------------")        
        tedad -= 1 
if ba_ki == "2":        
    if player1_score > player2_score:
            print(f"{name_1} win the game")
    if player1_score < player2_score:
            print (f"{name_2} win the game")
    if player2_score == player1_score:
            print ("draw") 
if ba_ki == "1":
    if player_score > computer_score:
        print ("player win the game")
    if computer_score > player_score:
        print ("computer win the game")
    if player_score == computer_score:
        print ("draw")                                                        
print ("!!! GAME OVER !!!") 
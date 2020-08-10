from random import randint
def printMessage():
    print("WELCOME TO Rock, Paper, Scissors, Lizard, Spock!\n\n")
    print("1. Play the Game\n\n")
    print("2. Learn more about the Game\n\n")
    print("3. Exit\n\n")
def winner(player,computer):
    if(player=='Rock' or 'rock'):
        if(computer=='Rock'):
            print("Computer chose Rock, Rocks collide and then fall and hence, it is a tie!\n\n")
            return 0
        elif(computer=='Paper'):
            print("Computer chose Paper, Paper covers Rock. Computer gets the point!\n\n")
            return -1
        elif(computer=='Lizard'):
            print("Computer summoned Lizard, Rock crushes Lizard. 1 point for you!\n\n")
            return 1
        elif(computer=='Spock'):
            print("Oops! Computer summoned Spock and Spock vaporised the Rock, Computer gets +1!\n\n")
            return -1
        else:
            print("Computer chose Scissors, you broke it with your Rock. You win!\n\n")
            return 1
    elif(player== 'Paper' or 'paper'):
        if(computer== 'Rock'):
            print("Computer chose Rock, Paper covers Rock, you win!\n\n")
            return 1
        elif(computer== 'Paper'):
            print("Computer chose Paper, you just threw Paper balls at each other. What are you, eight?. It's a tie\n\n")
            return 0
        elif(computer== 'Lizard'):
            print("Computer summoned Lizard, Lizard ate your Paper (lol). Computer wins.\n\n")
            return -1
        elif(computer== 'Spock'):
            print("Computer summoned Spock, Paper disproves Spock. 1 point for you!\n\n")
            return 1
        else:
            print("Computer chose Scissors, your Paper is now in shreds. Computer wins!\n\n")
            return -1
    elif(player== 'Scissors' or 'scissors'):
        if(computer == 'Rock'):
            print("Computer chose Rock, Rock crushed Scissors. Computer wins!\n\n")
            return -1
        elif(computer == 'Paper'):
            print("Computer chose Paper, Scissors cut paper. You win!\n\n")
            return 1
        elif(computer =='Lizard'):
            print("Computer summoned Lizard, Scissors decapitates Lizard. 1 point to you!\n\n")
            return 1
        elif(computer =='Spock'):
            print("Computer summoned Spock, Spock then smashed your Scissors. 1 point for the Computer!\n\n")
            return -1
        else:
            print("Computer chose Scissors, you scissors, scissored. It's a tie\n\n")
            return 0
    elif(player== 'Lizard' or 'lizard'):
        if(computer == 'Rock'):
            print("Computer chose Rock, Rock crushed Lizard. You now have a dead Lizard and  defeat against a robot. Computer wins!\n\n")
            return -1
        elif(computer == 'Paper'):
            print("Computer chose Paper, Lizard ate the Paper. You win!\n\n")
            return 1
        elif(computer =='Lizard'):
            print("Computer summoned Lizard, your Lizards are now BFFs. Its a tie!\n\n")
            return 0
        elif(computer =='Spock'):
            print("Computer summoned Spock, Your Lizard poisoned the Spock. You Win!\n\n")
            return 1
        else:
            print("Computer chose Scissors, Your Lizard just got decapitated. Computer wins.\n\n")
            return -1
    elif(player== 'Spock' or 'spock'):
        if(computer == 'Rock'):
            print("Computer chose Rock, your Spock vaporised the Rock. You Win!\n\n")
            return 1
        elif(computer == 'Paper'):
            print("Computer chose Paper, Paper disproves Spock. Computer wins!\n\n")
            return -1
        elif(computer =='Lizard'):
            print("Computer summoned Lizard, Lizard poisons the Spock. Computer wins!\n\n")
            return 1
        elif(computer =='Spock'):
            print("Computer summoned Spock, It got weird. Its a tie!\n\n")
            return 0
        else:
            print("Computer chose scissors, your Spock smashed Scissors. You win!\n\n")
            return 1
def computerChoose():
    number=randint(1,5)
    if(number==1):
        return 'Rock'
    elif(number==2):
        return 'Paper'
    elif(number==3):
        return 'Scissors'
    elif(number==4):
        return 'Lizard'
    else:
        return 'Spock'
def main():
    player_points=0
    computer_points=0
    player_choice=input("Make your Move! Choose btw (Rock/Paper/Scissors/Lizard/Spock)\n\n")
    computer_choice=computerChoose()
    b=True
    while(b):
        change=winner(player_choice,computer_choice)
        if(change==1):
            player_points+=1
        elif(change==-1):
            computer_points+=1
        print("Player Points= "+str(player_points)+" Computer Points= "+str(computer_points)+"\n\n")
        if(player_points==5 or computer_points==5):
            break
        else:
            player_choice=input("Make your Move! Choose btw (Rock/Paper/Scissors/Lizard/Spock)\n\n")
            computer_choice=computerChoose()
    if(player_points==5):
        print("CONGRATULATIONS, YOU WON!!")
    else:
        print("OOPS! COMPUTER WON!")

choice=0
while(choice!=3):
    printMessage()
    choice=int(input("Choose between (1/2/3)\n"))
    if(choice==1):
        main()
    elif(choice==2):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock\nThe game is an extension of the original game of 'Rock, Paper, Scissors'. It is a game of chance that expands.")
        print("The game was first mentioned on the popular sit-com ''The Big-Bang Theory'' in the episode ''The Lizard-Spock Expansion''.\nIt was used to settle a dispute about what to watch on TV between Sheldon and Raj.")
        print("The game is mentioned again by its creator, Sheldon in the episode ''The Rothman Disintegration'', where Sheldon explains the game to Penny and Barry Kripki.\n")
        print("Following are the rules of the game:\n\n")
        print("Scissors cuts Paper\n\nPaper covers Rock\n\nRock crushes Lizard\n\nLizard poisons Spock\n\nSpock smashes Scissors\n\nScissors decapitates Lizard\n\nLizard eats Paper\n\nPaper disproves Spock\n\nSpock vaporizes Rock\n\nand Rock crushes Scissors")
        print("\nYou are prompted to choose one of the five choices. The Computer then makes it's move.\nBased on the rules above, a point is provided to you or the Computer.\nThe first to reach 5 points wins the game!")
    elif(choice==3):
        print("Thank You for playing\nHave a good day.\n\nBazinga!")
    else:
        print("(-_-)\nChoose between (1/2/3)")


def repeat():

    wybor1 = input("Player1 enter you hand: ")
    wybor2 = input("Player2 Enter you hand: ")

    if wybor1 == "paper" and wybor2 == "rock":
        print("Player 1 win")
    elif wybor1 == "paper" and wybor2 == "scissors":
        print("Player 2 win")
    elif wybor1 == "paper" and wybor2 == "paper":
        print("Draw")
    elif wybor1 == "rock" and wybor2 == "paper":
        print("Player 2 win")
    elif wybor1 == "rock" and wybor2 == "scissors":
        print("Player 1 win")
    elif wybor1 == "rock" and wybor2 == "rock":
        print("Draw")
    elif wybor1 == "scissors" and wybor2 == "rock":
        print("Player 2 win")
    elif wybor1 == "scissors" and wybor2 == "paper":
        print("Player 1 win")
    elif wybor1 == "scissors" and wybor2 == "scissors":
        print("Draw")
    else:
        print("There in no such option")
    check = input("Do you want to continue? ")
    if check == "yes":
        repeat()
    else:
        exit()

repeat()








import random 
def com_choice() :
    options = ["snake" , "water" , "gun"]
    return random.choice(options)

def who_win(user_choice,computer_choice) :
    if user_choice == "snake" and computer_choice == "water":
        print("user won")
    elif user_choice == "water" and computer_choice == "gun":
        print("user won")
    elif user_choice == "gun" and computer_choice == "snake":
        print("user won")
    elif user_choice == computer_choice :
        print("Draw")
    else:
        print("computer won, user lost")


play = input("you want to play? ")
while play == "yes" or play == "y":
    user_choice = input("enter your choice please: ")
    computer_choice = com_choice()
    who_win(user_choice,computer_choice) 
    play = input("you want to play more ?  ")



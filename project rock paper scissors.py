import random


print('welcome to rock paper scissors ')
help = input(" type help for game rules ")
if help == "help":
    print('''******* RULES *******
          1) the computer will choose and you will choose at the same time
          2) rock beats scissors
          3) paper beats rock
          4) scissors beats paper
          5) if you choose the same as the computer then its draw
          ''')
    choice =(input("enter your choice rock paper or scissors "))
    if choice in("rock", "paper", "scissors"):
        choices =["rock", "scissors", "paper"]
        computer_choice = random.choice(choices)
        print(computer_choice)
        if computer_choice == "scissors" and choice =="paper":
            print(f"you lost! you chose {choice} while the computer chose {computer_choice}")
        elif computer_choice == "paper" and choice =="rock":
            print(f"you lost! you chose {choice} while the computer chose {computer_choice}")
        elif computer_choice == "rock" and choice == "scissors":
            print(f"you lost! you chose {choice} while the computer chose {computer_choice}")
        elif computer_choice == choice:
            print(f"Draw! you chose{choice} while the computer chose{computer_choice}")
        else:
            print(f"you win! the comuter chose {computer_choice} while you chose {choice} congrats! ")
else:
    print("invalid choice! please chose rock paper or scissors")


print('''
████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░██╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗██║
░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║██║
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║╚═╝
░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝██╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝''')
        
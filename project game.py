#welcome the user

print('''──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──

welcome to skull island
there been rumors about the lost treasure of skull island 
yet everyone whose gone to the island to try to find the lost treasure have been either found dead
or not found at all so lets begin the journey to try to find the lost treasure of skull island 
there are two doors infront of you 1 a red door 🧧 and a blue door 🟦  ''')
#ask user which door he wants to choose
while True:
    answer = input("which door do you want to choose ? \n")
    if answer == "blue":
        print("oops! you opened the crocodile door \n game over! 🐊🐊🐊")
        break
    else:
        if answer not in("blue", "red"):
            print("invalid choice! ")
#ask user which box he wants to choose
    if answer == "red":
        print("nice you enterd a secret room")
        print('"you found three boxes : 🎁 white, 🎁black, 🎁green "')
        boxes = input("which box do you choose ? \n")
        if boxes == "white":
            print("Oops! you opened a box full of snakes 🐍🐍🐍")
        elif boxes == "black":
            print("oops you opened a box full of spiders 🕷️🕷️🕷️ ")
        elif boxes == "green":
            print("congratulations! you found the lost treasure of skull island ! 💰💰💰 ")
            

        break   
print('''
                  

████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░██╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗██║
░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║██║
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║╚═╝
░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝██╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝''')
        





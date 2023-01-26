print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")


roadSplit = input("You are at a road splitting do you go middle left or right?\n")
if roadSplit == "left":
    print("you fell in a sink hole and died")
    print("The end")

if roadSplit == "right":
    print("A hungry lion jumped you, you are his meal")
    print("The end")

if roadSplit == "middle":
    riverChoice = input("You live! Now you encounter a river do you get on the spooky boat or swim across: type boat or swim\n")
    if riverChoice == "swim":
        islandchoice = input("Horay you made it to the island do you keep walking or dig?: type walk or dig\n")
        if islandchoice == "walk":
            print("You fall over a wooden box that turns out to be the treasure!")
            print("The end")
        else:
            print("You dig into lava!")
            print("The end")

    else:
        print("The captain sailed to the after world")
        print("The end")





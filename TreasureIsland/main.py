print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.")

left_or_right = input("You arrive at a crossroads. Which way do you want to go? Left or Right? ").lower()

if left_or_right == "left":
    swim_or_wait = input("You find yourself before an ominous lake. Will you wait for a boat or swim across? ").lower()
    if swim_or_wait == "wait":
        door_choice = input("You face 3 different doors(red, yellow, blue). Which one will you choose? ").lower()
        if door_choice == "red":
            print("Oops, you got burned by a fire trap.")
        elif door_choice == "yellow":
            print("Congratulations! You found the treasure!")
        elif door_choice == "blue":
            print("Ouch! You got eaten by some scary beasts!")
        else:
            print("Game over!")
    else:
        print("A mutated trout ate you!")
else:
    print("Darn, you fell into a bottomless pit!")
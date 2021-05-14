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
print("Your mission is to find the treasure.") 

left_or_right = input("You awaken in an empty field. There are no buildings in sight, only a path leading left or right. Which direction would you like to travel? Type 'left', or 'right'. \n").lower()
if left_or_right == "right":
    print("You walked off of a cliff and died. Game over.")
else:
    swim_or_wait = input("After hours of walking you arrive on the shore of a vast lake. Will you swim across or wait for a boat? Type 'swim' or 'wait'. \n").lower()
    if swim_or_wait == "swim":
        print("The depths of the lake contain great monsters and you were eaten within minutes of starting your swim. You're dead, game over. ")
    else:
        door_color = input("A boat arrived after an hour of waiting. It takes you to an enormous castle with three colored doors on the front. Which color door would you like to enter? Red, Blue, or Yellow? \n").lower()
        if door_color == "yellow":
            print("You open the yellow door and walk into a large room full of treasure. You help yourself to the riches and live the remainder of your life in splendor!!")
        else:
            print("The room is filled with trolls and ogres. They slaughter you immediatly and begin feasting on your corpse. Game over. ")

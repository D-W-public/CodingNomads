# Build a CLI RPG game following the instructions from the course.
import sys
# Ask the player for their name.
player_name = input("Please enter your name: ")

inventory = []

sword = "sword"
# Display a message that greets them and introduces them to the game world.
print(f"Welcome {player_name}. I hope you are ready for an adventure!", "\n","Let's go!")

print(
"You are ventureing down a dungeon, whith a torch in you hand.","\n", 
"The walls are scorched and there are bloody handprints everywhere.", "\n", 
"You follow the trail of carnage and find two doors."
)

door = None
# Present them with a choice between two doors.
while door == None:
    
    door = input(f"What door shall it be {player_name} \n Left or Right? \n").lower()
    door = door.lower()
# If they choose the left door, they'll see an empty room.
    if door == "left":
        interaction_1 = input("You found an empty room.\n Would you like to look arround, or would you rather go back? \n ")
        interaction_1 = interaction_1.lower()
        if interaction_1 == "look arround":
            print(f"You inspect the room and see something shining in a pile of bones. \n It's calling you. \n You pull a giant broad sword out of the pile. \n It looks like it was forged by a mastersmith for a nobleman \n ... \n No \n A KING! \n There is some thing etched on the blade\n DRAGONBANE \n You leave the room feeling like a million gold pieces.")
            inventory.append(sword)
            door = None
        elif interaction_1 == "go back":
            print("You walk back to the hallway... \n Empty handed!")
            door = None
# If they choose the right door, then they encounter a dragon.
    if door == "right":
        if sword in inventory:
            interaction_2 = input(f"The door opens with a big CRACKing sound. \n You look into a giant hall.\n There is a mountain of gold. \n You can't believ it. After all the hardships.\n The war. \n The plague. \n After you lost everyone you ever loved to the flames. \n This is the ticket for a new start. With tears of joy in your eyes \n Figth or Flight? ")
            interaction_2 = interaction_2.lower()
            if interaction_2 == "fight":
                print(f"The battle was long and fierce. The beats gave you all it got. But so did you. In a battle like this there can only be one winner. \n In this case \n You Lero.. äh.. {player_name} \n With it's dying breath the beast blasted a hole into the ceiling, opeming the dungein to the world above. \n You look up feel the sun shining on your scarred face. \n You take a deep breath. \n The air smells like blood and burnt flesh. \n You look on the mountain of gold. Your mountain of gold \n You vow to use it to build a better tomorrow for all who have sufferd from the war of the nine Kings. \n It's what she would have wanted. \n The end.")
            else:
                print("You lost. Fucking coward!")
                sys.exit()        
        elif sword not in inventory:
            interaction_3 = input("The door opens and you see a gigantic dragon sleeping on an even bigger pile of gold.\n You are alone and unarmed. \n In other words you're royalie fucked.\n What's it gonna be sissy? Fight or flight?")
            interaction_3 = interaction_3.lower()
            if interaction_3 == "fight":
                print("You are no match for the dragon. You are a brave kebap now. \n GAME OVER!")
                sys.exit()
            elif interaction_3 = "flight" or "go back":
                print(f"{player_name},you are a smart one. Hopefully you find something to aid your goals. \n You are back at the hallway.")
                door = None
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

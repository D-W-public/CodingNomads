# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

def game():
    player_name = input("Please enter your name: ")

    inventory = []

    sword = "sword"
# Display a message that greets them and introduces them to the game world.
    print(f"Welcome {player_name}. I hope you are ready for an adventure!", "\n","Let's go!")

    print("""
    You are ventureing down a dungeon, whith a torch in you hand. 
    
    The walls are scorched and there are bloody handprints everywhere. 
    
    You follow the trail of carnage and find two doors.""")

    door = True
# Present them with a choice between two doors.
    while door == True:
        
        door = input(f"What door shall it be {player_name} \n Left or Right? \n").lower()
        door = door.lower()
# If they choose the left door, they'll see an empty room.
# There is a hidden item, that can be found
        if door == "left":
            if sword in inventory:
                print("Don't be greedy. You found a weapon worhty of an Emperor.\n Back to the hallway with you")
                door = True

            elif sword not in inventory:    
                interaction_1 = input("You found an empty room.\n Would you like to look around, or would you rather go back? \n ")
                interaction_1 = interaction_1.lower()
                if interaction_1 == "look around":
                    print(f"""
                    You inspect the room and see something shining in a pile of bones.
                    It's calling you.
                    You pull a giant broad sword out of the pile.
                    It looks like it was forged by a mastersmith for a nobleman
                    
                    
                    No
                    
                    A KING!
                    
                    There is some thing etched on the blade
                    
                    DRAGONBANE
                    
                    You leave the room feeling like a million gold pieces.""")
                    
                    inventory.append(sword)
                    door = True
                elif interaction_1 == "go back":
                    print("You walk back to the hallway... \n Empty handed!")
                    door = True
                else:
                    door == "left"
# If they choose the right door, then they encounter a dragon.
# They can choose to fight or leave 
 
        if door == "right":
            if sword in inventory:
                interaction_2 = input(f"""
                The door opens with a big CRACKing sound.
                You look into a giant hall.
                There is a mountain of gold.
                You can't believ it. After all the hardships.
                
                The war.
                
                The plague.
                
                After you lost everyone you ever loved to the flames.
                This is the ticket for a new start. With tears of joy in your eyes,
                you look down on you brighley shining new sword.
                
                Brightley shining???

                Looking up you see a wall of fire rolling towards you.
                Rexxor the anihalater of realm has awoken from his slumber!!!
                
                In an adrenalin fueld second wind you shout to your self : 
                You can do this you are LEROY motherfucking JENKINS!!!


                Figth or Flight? \n """)
                interaction_2 = interaction_2.lower()
                if interaction_2 == "fight":
                    print(f"The battle was long and fierce. The beats gave you all it got. But so did you. In a battle like this there can only be one winner. \n In this case \n You Lero.. äh.. {player_name} \n With it's dying breath the beast blasted a hole into the ceiling, opeming the dungein to the world above. \n You look up feel the sun shining on your scarred face. \n You take a deep breath. \n The air smells like blood and burnt flesh. \n You look at the mountain of gold. Your mountain of gold \n You vow to use it to build a better tomorrow for all the victims of the Thousand year war. \n It's what she would have wanted. \n The end.")
                else:
                    print("You lost. Fucking coward!")
                    door = False        
            elif sword not in inventory:
                interaction_3 = input("""
                The door opens and you see a gigantic dragon sleeping on an even bigger pile of gold.
                
                You are alone and unarmed.
                
                In other words you're royalie fucked.
                
                What's it gonna be sissy? 
                Fight or flight? \n""")
                interaction_3 = interaction_3.lower()
                if interaction_3 == "fight":
                    print("You are no match for the dragon. You are a brave kebap now. \n GAME OVER!")
                    door = False
                elif interaction_3 == "flight" or "go back":
                    print(f"{player_name},you are a smart one. Hopefully you find something to aid your goals. \n You are back at the hallway.")
                    door = True


def main():
    game()
    while input("Would you like to play again? (Y/N)").upper == "Y":
        game()

if __name__ == "__main__":
    main()

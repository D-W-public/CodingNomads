# Build a CLI RPG game following the instructions from the course.
Flag = True
sword = "sword"
inventory = []
# Ask the player for their player_name.
player_name = str(input("Please enter your player_name: "))
player_name = player_name.capitalize()
# Display a message that greets them and introduces them to the game world.

print("""
You finaly come back to your senses. Your mouth tastes like blood an dirt.
Everythin is pitch black. Opening your eyes burns like hell.
You manage to get up by pushing through the pain and walk down a dimm hallway.
There are two doors in front of you.
""")

# Present them with a choice between two doors.

while Flag is True:
    door = str(
        input(f"""
Pick a door {player_name}
1) Left or 2) Right: """)
    )
    door = door.lower()

    # If they choose the left door, they'll see an empty room.

    if door in ["left", "1"]:
        if sword in inventory:
            print(f"Don't be a greedy coward, {player_name} ...")

            Flag = True

        elif sword not in inventory:
            choice_1_left_room = str(
                input("""
You enter an old study. It looks like its been looted
at least a dozen times. There is dried blood everywhere. You see scorch and claw marks on the scattered skeletons.
What do you want to do?
1) look around 2) go back: """)
            )

            choice_1_left_room = choice_1_left_room.lower()

            if choice_1_left_room in ["look around", "1"]:
                print("""
You start looking under broken furniture pieces. Push away rubble and body parts. 
It's exhausting. Your body is in tremendious pain.
Why?
Who knows.
Definetly not you.
From a crack in a wall you see some golden light flickering.
You go start exploring the wall and find one is loose. You press as hard as you can.
The entire room shakes and the wall opens op. In the distance there is a faint growl,
but you don't hear it. You are mezmerized by whats in front of you.
A shining altar with a glowing sword in the center. Underneath there is an iscription.

DRAGONBANE

You take your new weapon and feel it energy flowing throug your entire beeing.

Armed and ready you go back to the hallway.""")
                inventory.append(sword)

                Flag = True

            else:
                print("""
You go back to the hallway but it feels like unfinished buisness""")
                Flag = True

    # If they choose the right door, then they encounter a dragon.
    elif door in ["right", "2"]:
        choice_2_right_room = str(
            input(f"""
You enter a giant hall filled with piles of gold an gemstones.
In one of the piles you see an eye!!!

A dragons eye!

What will you do {player_name}?

1) Run
2) FIGHT
""")
        )
        choice_2_right_room = choice_2_right_room.lower()

        if choice_2_right_room in ["1", "run"]:
            print("You make it back to the hallway. Barley")
            Flag = True

        else:
            if sword in inventory:
                print(f"""
It was a firce battle. 
But you won.
{player_name} the Dragonslayer!""")
                break
            else:
                print("""
You were not prepared for this.
The dragon grills and eats you for lunch.

You lost the game...""")

                break


# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they =will be eaten by the dragon and lose the game.

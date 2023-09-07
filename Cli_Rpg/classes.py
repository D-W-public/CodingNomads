class Player:

    def __init__(self, name, hp, mana, armor, weapon, weapon_dmg):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.mana = mana
        self.weapon_dmg = weapon_dmg
        self.weapon = weapon
    
    def attack(self, other):
        other.hp -= (self.weapon_dmg/(other.armour/10))
        self.mana -= 15
    
    def item_pick_up(self, other):
        self.armor += other.armour
        self.weapon_dmg == other.weapon_dmg
        self.weapon == other.name
    
    def interact(self, other):
        print(other.description)
    

class Oponent(Player):

    def __init__(self, name, hp, armor, weapon_dmg):
        super.__init__(self, name, hp, armor, weapon_dmg)


class Weapon:

    def __init__(self, name, weapon_dmg):
        self.name = name
        self.weapon_dmg = weapon_dmg

class Armor:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor

class Item:
    def __init__(self, description):
        self.description = description

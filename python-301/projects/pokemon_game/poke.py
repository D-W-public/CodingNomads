
#create pokemon
class Pokemon:

    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hphp
        self.max_hp = max_hp

#inspect

    def __str__(self):
        return f"""
Name:               {self.name}
Type:               {self.primary_type}
Healthpoints:       {self.hp} / {self.max_hp}
"""
#feed/heal

    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 15
#FIGHT!

    def fight(self, other):
        prin(self.name, other.name)
        result = self.typewheel(self.primary_type, other.primary_type)
        
        

    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", -1: "tie"}
        #mapping conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}
        #implement win-lose matrix
        wl_matrix =[
            [-1, 1, 0] #water
            [0, -1, 1] #fire
            [1, 0, -1] #grass
        ]
        #declare winner
        
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]



if __name__ == "__main__":
    pass
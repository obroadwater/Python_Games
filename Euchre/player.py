# script to define the class of a player of the game
from hand import Hand

class Player:
    
    # name is a string, team will be string of either 1 or 2 (Euchre only involves 2 teams)
    def __init__(self, name, team):
        
        if not isinstance(name, str):
            raise Exception("Name must be a valid string")
        if team not in ['1', '2']:
            raise Exception("Team string must be either '1' or '2'")
        
        self.name = name
        self.team = team
        self.hand = Hand()
        
    def get_name(self):
        return self.name
    
    def get_team(self):
        return self.team
    
    def get_hand(self):
        return self.hand

# simple tests
'''p1 = Player("Owen", '1')

print(f"Player name is {p1.get_name()}, of team {p1.get_team()}: hand is currently {p1.get_hand().get_cards()}")

p2 = Player(0, '1')'''

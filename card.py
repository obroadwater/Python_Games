# Script to define the class of a singular card

class Card:
    
    # value, suit, and owner are all strings
    def __init__(self, value, suit, owner):
        if value not in ['9', '10', 'J', 'Q', 'K', 'A']:
            raise Exception('Card value outside the allowable range')
        if suit not in ['spades', 'clubs', 'hearts', 'diamonds']:
            raise Exception('Invalid suit')
        
        self.value = value
        self.suit = suit
        self.owner = owner
        
    def get_num_val(self, lead_suit = None, trump_suit = None):
        conversion = {"9": 0, "10": 1, "J": 2, "Q": 3, "K": 4, "A": 5}
        
        if self.value == "J":
            if self.suit == trump_suit:
                val = 12
            elif self.suit == "spades" and trump_suit == "clubs" or self.suit == "clubs" and trump_suit == "spades" or self.suit == "diamonds" and trump_suit == "hearts" or self.suit == "hearts" and trump_suit == "diamonds":
                val = 11
        else:
            if self.suit == trump_suit:
                val = conversion[self.value]
                val += 5 + (1 if val < 2 else 0)
            elif self.suit == lead_suit:
                val = conversion[self.value]
            else:
                val = -1
        return val
    
    def to_str(self):
        return f"{self.value} of {self.suit}"
    
    
'''x = Card(value = '9', suit = 'diamonds', owner = 'p1')
y = Card(value = 'J', suit = 'spades', owner = 'p1')
z = Card(value = 'A', suit = 'hearts', owner = 'p1')
a = Card(value = '10', suit = 'diamonds', owner = 'a')
b = Card(value = '10', suit = 'spades', owner = 'b')


tests = [("diamonds", "spades", x), ("spades", "clubs", y), ("diamonds", "hearts", z), ("diamonds", "diamonds", a), ("clubs", "hearts", b)]

for lead, trump, card in tests:
    print(f"Card {card.to_str()}: {lead} are led, {trump} is trump --> Card value == {card.get_num_val(lead, trump)}")        
        
        
print(x.to_str())'''
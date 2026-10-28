# script to define a collection of cards to be defined as a 'hand'
from card import Card

class Hand:
    
    # player is a Player object, cards is an array of Card objects
    def __init__(self, cards = [''] * 5):

        self.cards = cards
        self.cards_in_hand = len(cards)
        
        for i in range(len(cards)):
            if cards[i] == '':
                self.cards_in_hand = i
        
    def get_cards(self):
        return self.cards
    
    def get_hand_size(self):
        return self.cards_in_hand
    
    def add_card(self, card):
        if self.cards_in_hand == len(self.cards):
            print('Hand is full')
            return
        else:
            self.cards[self.cards_in_hand] = card
            self.cards_in_hand += 1
            
    def remove_card(self, card):
        for i in range(len(self.cards)):
            if self.cards[i].is_equal(card):
                temp = self.cards[i]
                self.cards[i] = ''
                self.cards_in_hand -= 1
                return temp
        print('Card not in the hand')
            
    def remove_card_idx(self, idx):
        temp = self.cards[idx]
        self.cards[idx] = ''
        self.cards_in_hand -= 1
        return temp
    
    
# not yet tested, will do after making the player class
x = Card(value = '9', suit = 'diamonds', owner = 'p1')
y = Card(value = 'J', suit = 'spades', owner = 'p1')
z = Card(value = 'A', suit = 'hearts', owner = 'p1')
a = Card(value = '10', suit = 'diamonds', owner = 'a')
b = Card(value = '10', suit = 'spades', owner = 'b')

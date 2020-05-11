class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} {self.suit}'

class DeckOfCards:

    def __init__(self):
        self._deck = []

        for suit in ['бубны', 'пики', 'черви', 'трефы']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9','10','J', 'Q','K']:
                self.full_deck.append(Card(suit, value))
        
        self.deck = self.full_deck.copy()

    
    def deal(self):
        deck = self.deck.copy()
        if not self.deck:
            print('No more cards in deck')
            return None
        return self.deck.pop()
    
    def mix(self):
        import random
        deck = self.full_deck.copy()
        return random.shuffle(deck)

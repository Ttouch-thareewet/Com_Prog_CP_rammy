class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "({} {})".format(self.value,self.suit)

    def next1(self):
        value_order = ('3', '4', '5', '6', '7', '8', '9', '10','J','Q','K','A','2')
        suit_order = ("club","diamond","heart","spade")
        if self.value == '2' and self.suit == 'spade': # 2 spade
            return Card('3','club')
        
        if suit_order.index(self.suit) != 3: # not 'spade'
            return Card(self.value,suit_order[1 + suit_order.index(self.suit)])
        else: # 'spade'
            return Card(value_order[1 + value_order.index(self.value)],'club')

    def next2(self):
        value_order = ('3', '4', '5', '6', '7', '8', '9', '10','J','Q','K','A','2')
        suit_order = ("club","diamond","heart","spade")

        if self.value == '2' and self.suit == 'spade': # 2 spade
            self.value = '3'
            self.suit = 'club'
        
        elif suit_order.index(self.suit) != 3: # not 'spade'
            self.suit = suit_order[1 + suit_order.index(self.suit)]

        else: # 'spade'
            self.value = value_order[1 + value_order.index(self.value)]
            self.suit = 'club'
        
n = int(input())
cards = []

for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].next1())
print("----------")

for i in range(n):
    print(cards[i])
print("----------")

for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
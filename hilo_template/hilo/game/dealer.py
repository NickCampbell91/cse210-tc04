import random

class Dealer:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.card = 0

    def can_deal(self):
        return (len(self.cards) > 0)

    def get_points(self):
        pass

    def deal_card(self):
        self.card = random.randint(1, len(self.cards))
        self.cards.pop(self.card - 1)
        return self.card

#print(f"{random.randint(1, len(self.cards))}")
# test = Dealer()
# print(test.cards)
# print(test.deal_card())
# print(test.cards)
# print(test.card)
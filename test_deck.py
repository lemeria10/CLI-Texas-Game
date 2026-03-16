from deck import Deck

deck = Deck()
deck.shuffle()

for _ in range(5):
    print(deck.deal())
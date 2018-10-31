# Deal 20 playing cards without replacement (16 tens, 36 low)
from collections import Counter
from random import sample

deck = Counter(tens=16, low=36)
deck = list(deck.elements())
deal = sample(deck, 20)
print(Counter(deal))

# Counting cards to win blackjack
deal = sample(deck, 52)
remainder = deal[20:]
print(Counter(remainder))

import random
def deal_card():
  #cards aren't removed from the deck after being draw, can be repeated.
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  dealed_card = random.choice(cards)
  return dealed_card

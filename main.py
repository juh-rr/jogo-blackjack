from art import logo
from dealcard import deal_card
from calculatescore import calculate_score
from firstround import first_round
from checkwinner import check_winner

#REGRAS DO JOGO
#Cartas podem ser repetidas
#Se a soma das cartas do computador for menor que 17, o computador irá puxar cartas até atingir esse valor mínimo
#O ás tem valor de 11, porém se a soma das cartas + o ás for maior que 21, o valor dele muda para 1

user_cards = []
computer_cards = []
print(logo)
first_round(user_cards)
first_round(computer_cards)
print("Welcome to Blackjack! Here's your first hand:")
print(user_cards)
print("Here's the computer's hand:")
print(f"[{computer_cards[0]}, X]")

if calculate_score(user_cards) < 21:
  keep_drawing = True

while keep_drawing:
  another_draw = input("Do you wish to draw another card? Type 'y' or 'n': ").lower()
  if another_draw == "y":
    user_cards.append(deal_card())
    print(user_cards)
    if calculate_score(user_cards) > 21:
      keep_drawing = False
      check_winner(user=user_cards, computer=computer_cards)
  elif another_draw == "n":
    keep_drawing = False
    check_winner(user=user_cards, computer=computer_cards)
  else:
    print("Please type a valid answer.")

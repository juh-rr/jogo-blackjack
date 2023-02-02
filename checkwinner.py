from dealcard import deal_card
from calculatescore import calculate_score

def check_winner(user, computer):
  #If the sum of computer cards is less than 17, keep drawing
  while sum(computer) < 17:
    computer.append(deal_card())
    
  final_score_user = calculate_score(user)
  final_score_pc = calculate_score(computer)
  
  print(f"Your cards are: {user}")
  print(f"Your final score is: {final_score_user}")
  print(f"The computer cards are: {computer}")
  print(f"The computer final score is: {final_score_pc}")
  if final_score_user > 21:
    print("It's a bust! You lose!")
  elif final_score_pc > 21:
    print("It's a bust for the computer, you win!")
  elif final_score_pc == 0 and final_score_user == 0:
    print("You both got a blackjack! It's a draw!")
  elif final_score_user == 0:
    print("You got a blackjack! You win!")
  elif final_score_pc == 0:
    print("The computer got a blackjack! The computer wins!")
  elif final_score_pc > final_score_user:
    print("The computer has a number closer to 21! The computer wins!")
  elif final_score_pc == final_score_user:
    print("You both have the same number! It's a draw!")
  else:
    print("You have a number closer to 21! You win!")

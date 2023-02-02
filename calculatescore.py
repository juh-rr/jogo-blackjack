def calculate_score(user):
  blackjack = 0
  total_score = 0
  #if total_score is 21, use blackjack
  #Check if 10 + ace
  if len(user) == 2 and sum(user) == 21:
    return blackjack
  #check if score + 21,and if there's an ace(11), exchange ace for 1
  elif sum(user) > 21:
    for i in user:
      if i == 11:
        user.remove(11)
        user.append(1)
        total_score = sum(user)
        if total_score == 21:
          return blackjack
        else:
          return total_score
    else: 
      total_score = sum(user)
      return total_score
  else:
    total_score = sum(user)
    if total_score == 21:
      return blackjack
    else:
      return total_score

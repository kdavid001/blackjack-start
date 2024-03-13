

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
user_cards = random.sample(cards,2)
computer_cards = random.sample(cards,1)
print(f"Your cards: {user_cards}")
print(f"computer's first card: {computer_cards}")
computer_cards.append(random.choice(cards))
print(f"computer's cards: {computer_cards}")

#user_cards = []
#computer_cards = []

def calculated_score():
  user_sum = sum(user_cards)
  computer_sum = sum(computer_cards)
  blackjack = 0
   
  for n in range(len(user_cards)) or range(len(computer_cards)):
    if user_cards[n] == 11 and user_cards[n] == 10:
      user_sum = 0
    elif computer_cards[n] == 11 and computer_cards[n]== 10:
      computer_sum = 0
   
      
    if user_cards[n] == 11 and user_sum > 21:
      user_cards[n] = 1
  print(user_sum)
  print(computer_sum)
      
calculated_score()


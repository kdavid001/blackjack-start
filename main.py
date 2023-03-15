############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from art import logo
from replit import clear
def start_game():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
  
  def deal_card():
    random_card = random.choice(cards)
    return random_card
    
    
    
  
  
  print(logo)
  user_cards = random.sample(cards,2)
  computer_cards = random.sample(cards,1)
  print(f"Your cards: {user_cards}")
  print(f"your score {sum(user_cards)}")
  print(f"computer's first card: {computer_cards}")
  computer_cards.append(random.choice(cards))
  
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  
  #user_cards = []
  #computer_cards = []
  
  #Hint 6: Create a function called calculate_score() that takes a List of cards as input
  def calculated_score():
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)
    
    if user_cards[0] == 11 and user_cards[1] == 10:
      user_sum = 0 
    if computer_cards[0] == 11 and computer_cards[1]== 10:
      computer_sum = 0
     
    for n in range(len(user_cards)) or range(len(computer_cards)):
      if user_cards[n] == 11 and user_sum > 21:
        user_cards[n] = 1
        user_sum = sum(user_cards)
      if computer_cards[n] == 11 and computer_sum > 21:
        computer_cards[n] = 1
        computer_sum = sum(computer_cards)
  
    return user_sum,computer_sum
    
        
  user_sum, computer_sum = calculated_score()
  
  if (computer_sum or user_sum) == 0:
    game_end = True
    print("Game has ended")
  if (computer_sum or user_sum) > 21:
    game_end = True
    print("Game has ended")
  else:
    game_end = False
  while game_end == False:
    
    draw_card = input("Do you want to draw another card, type 'y' for yes and 'n' for no ").lower()
    if draw_card == 'y':
      user_cards.append(deal_card())
      print(f"Your cards: {user_cards}")
      user_sum = sum(user_cards)
      print(user_sum)
      if user_sum > 21:
        game_end = True
    if draw_card == 'n':
      game_end = True
  
  while computer_sum < 17:
    computer_cards.append(deal_card())
    computer_sum = sum(computer_cards)
    print(f"computer's cards: {computer_cards}")
    
  
  def compare(user_sum,computer_sum):
    if user_sum == computer_sum:
      print("it's a draw")
    if user_sum == 0:
      print("blackjack, You win!")
    elif computer_sum == 0:
      print("blackjack, You lose!")
    if user_sum > 21:
      print("You lose!")
    elif computer_sum > 21:
      print("you win")
    if user_sum > 21 and computer_sum > 21:
      if user_sum > computer_sum:
        print("you win!")
      elif computer_sum > user_sum:
        print("You lose!")
  
     
  print(f"your score {sum(user_cards)}")     
  print(f"computer score: {computer_sum}")
  compare(user_sum,computer_sum)


start_game()
restart = input("Do you want to restart the game? type 'y' for yes and 'n' for no")
if restart == 'y':
    clear()
    start_game()

#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


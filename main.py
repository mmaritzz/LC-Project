import random
import time # time.sleep(1)
import csv
import matplotlib.pyplot as plt
import numpy as np
from art import *
import sys


animation = ["Welcome to.","Welcome to..", "Welcome to..."]

print("\n\n")

for i in range(len(animation)):
    time.sleep(0.6)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

time.sleep(1)
print("\n")


Art1=text2art("Blackjack", font="cards")
print(Art1)
time.sleep(1)

print("\n\n\nPlease select a game mode:\n")
print("1. Singleplayer")
print("2. Multiplayer")
print("3. Autonomous")
time.sleep(.5)

game_mode = input("\nEnter your choice (1, 2, or 3): ")
time.sleep(.5)

# Singleplayer
if game_mode == "1":


  animation = ["Starting Singleplayer game.","Starting Singleplayer game..", "Starting Singleplayer game..."]

  print("\n\n")
  for i in range(len(animation)):
      time.sleep(.6)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()

  time.sleep(1)
  print("\n")
  
  deck = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
  deck *= 4

# takes a number of cards to deal and returns a list of strings representing the cards
  def deal_cards(num_cards):
    return [str(card) for card in random.sample(deck, num_cards)]

# takes a list of cards and calculates the value of the hand according to the rules of Blackjack
  def hand_value(hand):
    value = 0
    num_aces = 0
  
    for card in hand:
      if card in ['J', 'Q', 'K']:
        value += 10
      elif card == 'A':
        num_aces += 1
      else:
        value += int(card)
  
    for i in range(num_aces):
      if value + 11 <= 21:
        value += 11
      else:
        value += 1
  
    return value

# takes a list of cards and displays them on the screen
  def display_hand(hand, player_name=None, above=False, is_dealer=False, show_all=True):
    if above and is_dealer:
      print("Dealer's hand: ", end="")
    if player_name:
      print(f"{player_name}'s hand: ", end="")
      for card in hand:
        print(str(card) + " ", end="")
      print(f"({hand_value(hand)})")
    elif not above and not is_dealer:
      for i, card in enumerate(hand):
        if i == 0 and show_all:
          print(str(card) + " ", end="")
        elif i == 0 and not show_all:
          print("[hidden] ", end="")
        else:
          print(str(card) + " ", end="")
      print(f"({hand_value(hand)})")
    elif not above and is_dealer:
      print("\nDealer's hand: ", end="")
      print("[hidden] " if show_all else str(hand[0]) + " ", end="")
      print(f"({hand_value([hand[0]])})", end="")
    else:
      for i, card in enumerate(hand):
        if i == 0 and above:
          print(str(card) + " ", end="")
        elif i == 0 and not above and not show_all:
          print("[hidden] ", end="")
        else:
          print(str(card) + " ", end="")
      if not above and not show_all:
        print("[hidden] ", end="")
      print(f"({hand_value(hand)})")

# represents the player's turn in the game
  def player_turn(dealer_hand):
    player_hand = deal_cards(2)
    print("Dealer's hand:")
    print(str(dealer_hand[0]) + " [hidden] ", end="")
    time.sleep(.5)
    print("\n\nYour hand:", "\n", end=' ')
    display_hand(player_hand, is_dealer=False, above=True, show_all=True)
    time.sleep(.5)
  
    while True:
      if hand_value(player_hand) > 21:
        print("Bust! You lose.")
        time.sleep(1)
        return []
      time.sleep(.5)
      choice = input("\nDo you want to (h)it or (s)tand? ")
      if choice.lower() == 'hit' or choice.lower() == 'h':
        player_hand += deal_cards(1)
        print("\nYour hand:", "\n", end=' ')
        display_hand(player_hand, is_dealer=False, above=True, show_all=True)
      elif choice.lower() == 'stand' or choice.lower() == 's':
        print("\nYour final hand:", end=' ')
        display_hand(player_hand, is_dealer=False)
      else:
        print("Error. Please hit or stand.")
        time.sleep(1)
        exit()
  
    return player_hand

# represents the dealer's turn in the game
  def dealer_turn(player_hand, dealer_hand):
    print("\n\nDealer's hand:")
    display_hand(dealer_hand)
    time.sleep(.5)
  
    while hand_value(dealer_hand) < 17:
      dealer_hand += deal_cards(1)
      print("\nDealer hits:")
      display_hand(dealer_hand)
  
# deals two cards to both the player and the dealer and returns the dealer's hand and the player's hand
  def deal_initial_hands():
    dealer_hand = deal_cards(2)
    player_hand = deal_cards(2)
    return dealer_hand, player_hand
  
# This function is the main program that runs the game
  def main():
    
    print("\nWelcome to  Singleplayer Blackjack!\n\n")
    time.sleep(1)

    dealer_hand, player_hand = deal_initial_hands()
  


    h = 1
    while h == 1:   
  

      player_hand = player_turn(dealer_hand)
      if hand_value(player_hand) == 21:
          print("You have a blackjack! You win!")
  
      dealer_turn(player_hand, dealer_hand)
      if hand_value(dealer_hand) == 21:
          print("Dealer has blackjack! You lose!")

      player_value = hand_value(player_hand)
      dealer_value = hand_value(dealer_hand)
     
  
      if dealer_value > 21:
        print("\nDealer busts! You win!")
      elif dealer_value > player_value:
        print("\nDealer wins!")
      elif dealer_value < player_value:
        print("\nYou win!")
      else:
        print("\nIt's a tie!")
      break

    play_again = input("Do you want to play again? (Y/N) ").lower()
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")
        exit()
    
  main()

# Multiplayer
elif game_mode == "2":

  animation = ["Starting Multiplayer game.","Starting Multiplayerr game..", "Starting Multiplayer game..."]

  print("\n\n")

  for i in range(len(animation)):
      time.sleep(.6)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()

  time.sleep(1)
  print("\n")

  deck = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
  deck *= 4

# takes a number of cards to deal and returns a list of strings representing the cards
  def deal_cards(num_cards):
    return [str(card) for card in random.sample(deck, num_cards)]

# takes a list of cards and calculates the value of the hand according to the rules of Blackjack
  def hand_value(hand):
      value = 0
      num_aces = 0
  
      for card in hand:
          if card in ['J', 'Q', 'K']:
              value += 10
          elif card == 'A':
              num_aces += 1
          else:
              value += int(card)
  
      for i in range(num_aces):
          if value + 11 <= 21:
              value += 11
          else:
              value += 1
  
      return value
  
# takes a list of cards and displays them on the screen
  def display_hand(hand, player_name=None, above=False, is_dealer=False, show_all=True):
    if above and is_dealer:
      print("Dealer's hand: ", end="")
    if player_name:
      for card in hand:
        print(str(card) + " ", end="")
      print(f"({hand_value(hand)})")
  
      
    elif not above and not is_dealer:
      for i, card in enumerate(hand):
        if i == 0 and show_all:
          print(str(card) + " ", end="")
        elif i == 0 and not show_all:
          print("[hidden] ", end="")
        else:
          print(str(card) + " ", end="")
      print(f"({hand_value(hand)})")
    elif not above and is_dealer:
      print("\nDealer's hand: ", end="")
      print("[hidden] " if show_all else str(hand[0]) + " ", end="")
      print(f"({hand_value([hand[0]])})", end="")
    else:
      for i, card in enumerate(hand):
        if i == 0 and above:
          print(str(card) + " ", end="")
        elif i == 0 and not above and not show_all:
          print("[hidden] ", end="")
        else:
          print(str(card) + " ", end="")
      if not above and not show_all:
        print("[hidden] ", end="")
      print(f"({hand_value(hand)})")
  
# represents the player 1's turn in the game
  def player_turn_1(player1_hand, dealer_hand):
      player1_hand = deal_cards(2)
      print("\n\nDealer's hand:")
      print(str(dealer_hand[0]) + " [hidden] ", end="")
      print("\n\nPlayer 1's hand:", "\n", end=' ')
      display_hand(player1_hand, player_name="Player 1", is_dealer=False, above=True, show_all=True)
  
      while True:
          if hand_value(player1_hand) > 21:
              print("Bust! Player 1 loses.")
              time.sleep(1)
              return []
  
          choice = input("\nPlayer 1, do you want to (h)it or (s)tand? ")
          if choice.lower() == 'hit' or choice.lower() == 'h':
              player1_hand += deal_cards(1)
              print("\nPlayer 1's hand:", "\n", end=' ')
              display_hand(player1_hand, player_name="Player 1", is_dealer=False, above=True, show_all=True)
          elif choice.lower() == 'stand' or choice.lower() == 's':
              print("\nPlayer 1's final hand:", end=' ')
              display_hand(player1_hand, player_name="Player 1", is_dealer=False)
          else:
              print("Error. Please hit or stand.")
              time.sleep(1)
              exit()
  
      return player1_hand
  
# represents the player 2's turn in the game
  def player_turn_2(player2_hand, dealer_hand):
    player_hand = deal_cards(2)
    print("\n\nDealer's hand:")
    print(str(dealer_hand[0]) + " [hidden] ", end="")
    print("\n\nPlayer 2's hand:", "\n", end=' ')
    display_hand(player_hand, player_name="Player 2", is_dealer=False, above=True, show_all=True)
  
    while True:
      if hand_value(player_hand) > 21:
        print("Bust! Player 2 loses.")
        time.sleep(1)
        return []
  
      choice = input("\nPlayer 2, do you want to (h)it or (s)tand? ")
      if choice.lower() == 'hit' or choice.lower() == 'h':
        player_hand += deal_cards(1)
        print("\nPlayer 2's hand:", "\n", end=' ')
        display_hand(player_hand, player_name="Player 2", is_dealer=False, above=True, show_all=True)
      elif choice.lower() == 'stand' or choice.lower() == 's':
        print("\nPlayer 2's final hand:", end=' ')
        display_hand(player_hand, player_name="Player 2", is_dealer=False)
        break
  
    return player_hand
  
# represents the dealer's turn in the game
  def dealer_turn(dealer_hand):
    print("\n\nDealer's hand:")
    display_hand(dealer_hand)
  
    while hand_value(dealer_hand) < 17:
      dealer_hand += deal_cards(1)
      print("\nDealer hits:")
      display_hand(dealer_hand)

# deals two cards to both the player's and the dealer and returns the dealer's hand and the player's hand's
  def deal_initial_hands():
    dealer_hand = deal_cards(2)
    player1_hand = deal_cards(2)
    player2_hand = deal_cards(2)
    return dealer_hand, player1_hand, player2_hand
  
# determins the winner of the game in every possibe outcome
  def determine_winner(player1_hand, player2_hand, dealer_hand):
      player1_value = hand_value(player1_hand)
      player2_value = hand_value(player2_hand)
      dealer_value = hand_value(dealer_hand)
      
      if player1_value > 21:
          if player2_value > 21:
              print("Both players bust! Dealer wins!")
          else:
              print("Player 1 busts! Player 2 wins!")
      elif player2_value > 21:
          print("Player 2 busts! Player 1 wins!")
      else:
          if dealer_value > 21:
              if player1_value == player2_value:
                  print("Both players win! Dealer busts!")
              elif player1_value > player2_value:
                  print("Player 1 wins! Both players beat the dealer!")
              else:
                  print("Player 2 wins! Both players beat the dealer!")
          else:
              if dealer_value == player1_value == player2_value:
                  print("It's a three-way tie!")
              elif dealer_value == player1_value:
                  if dealer_value > player2_value:
                      print("Dealer and Player 1 tie! Dealer wins against Player 2!")
                  elif dealer_value < player2_value:
                      print("Dealer and Player 2 tie! Player 2 wins against Player 1!")
              elif dealer_value == player2_value:
                  if dealer_value > player1_value:
                      print("Dealer and Player 2 tie! Dealer wins against Player 1!")
                  elif dealer_value < player1_value:
                      print("Dealer and Player 1 tie! Player 1 wins against Player 2!")
              elif player1_value == player2_value:
                  if player1_value > dealer_value:
                      print("Both players win against Dealer!")
                  else:
                      print("Dealer wins against both players!")
              else:
                  if dealer_value > player1_value and dealer_value > player2_value:
                      print("Dealer wins against both players!")
                  elif player1_value > dealer_value and player1_value > player2_value:
                      print("Player 1 wins!")
                  elif player2_value > dealer_value and player2_value > player1_value:
                      print("Player 2 wins!")
                  else:
                      print("It's a tie!")
   
# This function is the main program that runs the game
  def main():
      
      print("Welcome to  Multiplayer Blackjack!\n")
      time.sleep(.5)
    
      player1_hand = []
      player2_hand = []
      dealer_hand = []
  
      player1_hand, player2_hand, dealer_hand = deal_initial_hands()
  
      player_turn_1(player1_hand, dealer_hand)
      player_turn_2(player2_hand, dealer_hand)
      dealer_turn(dealer_hand)
      determine_winner(player1_hand, player2_hand, dealer_hand)
  
      play_again = input("Do you want to play again? (Y/N) ").lower()
      if play_again == "y":
          main()
      else:
          print("Thanks for playing!")
          exit()

  main()

# Autonomous
elif game_mode == "3":

  animation = ["Starting Autonomous game.","Starting Autonomous game..", "Starting Autonomous game..."]

  print("\n\n")

  for i in range(len(animation)):
      time.sleep(.6)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()

  time.sleep(1)
  print("\n")

  deck = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
  deck *= 4


# takes a number of cards to deal and returns a list of strings representing the cards
  def deal_cards(num_cards):
      return [str(card) for card in random.sample(deck, num_cards)]
  
# takes a list of cards and calculates the value of the hand according to the rules of Blackjack
  def hand_value(hand):
      value = 0
      num_aces = 0
  
      for card in hand:
          if card in ['J', 'Q', 'K']:
              value += 10
          elif card == 'A':
              num_aces += 1
          else:
              value += int(card)
  
      for i in range(num_aces):
          if value + 11 <= 21:
              value += 11
          else:
              value += 1
  
      return value
  
# represents the autoplayer's turn in the game
  def autoplayer_turn(player_hand, player_stand):
      
      while True:
          if hand_value(player_hand) > 21:
              return [22]
          if hand_value(player_hand) >= player_stand:
              break
          else:
              player_hand += deal_cards(1)

      return player_hand

# represents the autodealer's turn in the game
  def autodealer_turn(dealer_hand,):
      while hand_value(dealer_hand) < 17:
          dealer_hand += deal_cards(1)
      return dealer_hand

# determines the winner
  def determine_winner(player_hand, dealer_hand):

    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)


    if player_total > 21:
        return "Dealer"
    elif dealer_total > 21:
        return "Player"
    elif player_total > dealer_total:
        return "Player"
    elif dealer_total > player_total:
        return "Dealer"
    else:
        return "Tie"

# deals two cards to both the autoplayer and the autodealer and returns the autodealer's hand and the autoplayer's hand
  def deal_initial_hands():
      dealer_hand = deal_cards(2)
      player_hand = deal_cards(2)
      return dealer_hand, player_hand
  
# This function is the main program that runs the game
  def main():
      
      print("\nWelcome to  Autonomous Blackjack!")
      time.sleep(.5)

      num_games = int(input("\n\nHow many games would you like to play? "))

      global player_stand
      player_stand = int(input("At what value would you like for the player to hold? "))
  
      with open('blackjack_results.csv', mode='w') as file:
          writer = csv.writer(file, lineterminator = '\n')
          writer.writerow(["Game", "Dealer Win", "Player Win", "Ties", "Dealer Blackjack", "Player Blackjack", "No blackjack"])


          player_wins = 0
          dealer_wins = 0
          ties = 0
          dealer_bj = 0
          player_bj = 0


  
          for game in range(num_games):
              dealer_wins_game = False
              player_wins_game = False
              tie_game = False
              dealer_bj_game = False
              player_bj_game = False

              dealer_hand, player_hand = deal_initial_hands()
              
              print(game)
            
              # Check for dealer blackjack
              if hand_value(dealer_hand) == 21:
                  dealer_bj_game = True
                  dealer_bj += 1
                  
  
              # Check for player blackjack
              if hand_value(player_hand) == 21:
                  player_bj_game = True
                  player_bj += 1
  
              # Player's turn
              player_hand = autoplayer_turn(player_hand, player_stand)

              # Dealer's turn
              dealer_hand = autodealer_turn(dealer_hand)    

              winner = determine_winner(player_hand, dealer_hand)
              if winner == "Player":
                  print("Player wins!")
                  player_wins_game = True
                  player_wins += 1
              elif winner == "Dealer":
                  print("Dealer wins!")
                  dealer_wins_game = True
                  dealer_wins += 1
              else:
                  print("Tie!")
                  tie_game = True
                  ties += 1

  
              # Print game results
              writer.writerow([game+1, dealer_wins_game, player_wins_game, tie_game, dealer_bj_game, player_bj_game, not(dealer_bj_game or player_bj_game)])

              num_no_blackjack = int(num_games) - (int(dealer_bj) + int(player_bj))
              total_bj = int(dealer_bj) + int(player_bj)

          # Display final results
          print("\n--- Final Results ---\n")
          time.sleep(2)
          print(f"Player Stand: {player_stand}")
          print(f"Player Wins: {player_wins}")
          print(f"Dealer Wins: {dealer_wins}")
          print(f"Ties: {ties}")
          print(f"Total Blackjacks: {total_bj}")
          print("Check .csv for more info. More info displayed on graphs via matplotlib")
          print("\n------- DONE -------\n")

          time.sleep(1)

          y = np.array([dealer_bj, player_bj, num_no_blackjack])
          ylabels = ["Dealer Blackjacks", "Player Blackjacks", "No Blackjacks"]
          explode = (0.05, 0.05, 0)

          fig, ax = plt.subplots()
          plt.pie(y, labels = ylabels, explode=explode, autopct='%1.1f%%', textprops={'fontsize': 7}, radius=.7, startangle=90, colors=['black', 'red', 'green'])
          
          ax.legend(ylabels, title="Legend", loc="center right", bbox_to_anchor=(0.8, 0, 0.5, 1))

          fig.set_facecolor('#4f4f4f')
          ax.set_title('Chances of a blackjack compared to no blackjack')

          for text in ax.texts:
            text.set_color('yellow')

          z = np.array([player_wins, dealer_wins, ties])
          zlabels = ["Wins", "Losses", "Ties"]
          explode = (0, 0, 0)

          fig, ax = plt.subplots()
          plt.pie(z, labels = zlabels, explode=explode, autopct='%1.1f%%', textprops={'fontsize': 7}, radius=.7, startangle=90, colors=['blue', 'red', 'yellow'])

          ax.legend(zlabels, title="Legend", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 1))

          fig.set_facecolor('#4f4f4f')
          ax.set_title('Chance of Winning')

          for text in ax.texts:
            text.set_color('black')

          plt.show() 
  
  if __name__ == "__main__":
    main()

else:
    
    print("Error. Please enter 1, 2, or 3.")
    time.sleep(1)


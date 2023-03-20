# Import necessary modules
import random
import time # pip install python-time
import csv # pip install python-csv
import matplotlib.pyplot as plt # pip install matplotlib
from PIL import Image # pip install Pillow
import numpy as np # pip install numpy
from art import *  # pip install art==5.9
from rich.console import Console # pip install rich
import sys # pip install os-sys
import os

# Define the 'Welcome to' animation sequence
animation = ["Welcome to.","Welcome to..", "Welcome to..."]

# Print the animation sequence
print("\n\n")

for i in range(len(animation)):
    time.sleep(0.6)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

time.sleep(1)
print("\n")

# Generate ASCII art title
Art1=text2art("Blackjack", font="cards")
print(Art1)
time.sleep(1)

# Prompt the user to select a game mode
print("\n\n\nPlease select a game mode:\n")
time.sleep(.3)
print("1. Singleplayer")
time.sleep(.3)
print("2. Multiplayer")
time.sleep(.3)
print("3. Autonomous")

# Get the user's game mode choice
game_mode = input("\nEnter your choice (1, 2, or 3): ")

time.sleep(.5)

# singleplayer
if game_mode == "1":

    # Define the singleplayer animation sequence
    animation = ["Starting Singleplayer game.", "Starting Singleplayer game..", "Starting Singleplayer game..."]

    # Print the animation sequence
    print("\n\n")

    for i in range(len(animation)):
        time.sleep(0.6)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    time.sleep(1)
    print("\n")

    # Print a welcome message
    print("\nWelcome to Singleplayer Blackjack!\n\n")
    time.sleep(1)

    # Define the deck of cards for singleplayer mode
    deck = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    deck *= 4


    # takes a number of cards to deal and returns a list of strings representing the cards
    def deal_cards(num_cards):
        time.sleep(0.5)
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

        for _ in range(num_aces):
            value += 11 if value <= 10 else 1
        return value

    # A function that takes a list of cards and displays them on the screen
    def display_hand(hand, player_name=None, above=False, is_dealer=False, show_all=True):

        # If above and is_dealer are True, display "Dealer's hand"
        if above and is_dealer:
            print("Dealer's hand: ", end="")

        # If player_name is not None, display "{player_name}'s hand"
        if player_name:
            print(f"{player_name}'s hand: ", end="")
            for card in hand:
                print(f"{str(card)} ", end="")
                time.sleep(0.5)
            print(f"({hand_value(hand)})")

        # If above and is_dealer are False and show_all is True, display all cards in the hand
        elif not above and not is_dealer:
            for i, card in enumerate(hand):
                if i == 0 and show_all or i != 0:
                    print(f"{str(card)} ", end="")
                else:
                    print("[hidden] ", end="")
                time.sleep(0.5)
            print(f"({hand_value(hand)})")

        # If above is False and is_dealer is True, display only the first card in the dealer's hand
        elif not above:
            print("\nDealer's hand: ", end="")
            print("[hidden] " if show_all else f"{str(hand[0])} ", end="")
            time.sleep(0.5)
            print(f"({hand_value([hand[0]])})", end="")

        # If above is True, display all cards in the hand except the first one
        else:
            for i, card in enumerate(hand):
                if i == 0 and above or i != 0 or show_all:
                    print(f"{str(card)} ", end="")
                else:
                    print("[hidden] ", end="")
                time.sleep(0.5)

            # If above and show_all are False, display the first card as hidden
            if not above and not show_all:
                print("[hidden] ", end="")
                time.sleep(0.5)
            print(f"({hand_value(hand)})")  

    # represents the player's turn in the game
    def player_turn(dealer_hand):

        # deal two cards to the player
        player_hand = deal_cards(2)

        # Display the dealer's first card and hide the second one
        print("\n\nDealer's hand:")
        print(f"{str(dealer_hand[0])} [hidden] ", end="")
        time.sleep(0.5)
        
        # Display the player's hand
        print("\n\nYour hand:", "\n", end=' ')
        display_hand(player_hand, is_dealer=False, above=True, show_all=True)
        time.sleep(0.5)

        # Keep asking the player if they want to hit or stand until they stand or bust
        while True:

            # Check if the player busts
            if hand_value(player_hand) > 21:
                print("Bust! You lose.")
                time.sleep(1)
                return []

            # Asks the player if they want to hit or stand
            time.sleep(0.5)
            choice = input("\nDo you want to (h)it or (s)tand? ")

            # If the player chooses to hit, deal another card and display the hand
            if choice.lower() in ['hit', 'h']:
                player_hand += deal_cards(1)
                print("\nYour hand:", "\n", end=' ')
                display_hand(player_hand, is_dealer=False, above=True, show_all=True)

            # If the player chooses to stand, display the final hand and exit the loop
            elif choice.lower() in ['stand', 's']:
                print("\nYour final hand:", end=' ')
                display_hand(player_hand, is_dealer=False)
                break

            # If the player enters an invalid input, display an error message and exit the program
            else:
                print("Error. Please hit or stand.\n\n")
                time.sleep(1)
                exit()

        return player_hand

    # represents the dealer's turn in the game
    def dealer_turn(dealer_hand):

        # display the dealer's hand
        print("\n\nDealer's hand:")
        display_hand(dealer_hand)
        time.sleep(.5)

        # The dealer hits as long as the hand value is less than 17
        while hand_value(dealer_hand) < 17:
            dealer_hand += deal_cards(1)
            print("\nDealer hits:\n")
            display_hand(dealer_hand)
            print("\n")
            time.sleep(1)

    # deals two cards to both the player and the dealer and returns the dealer's hand and the player's hand
    def deal_initial_hands():
        dealer_hand = deal_cards(2)
        player_hand = deal_cards(2)
        return dealer_hand, player_hand

    # Define the main function
    def main():

        # Deal the initial hands to the dealer and player
        dealer_hand, player_hand = deal_initial_hands()

        # Start a loop to continue playing until the game is over
        h = 1
        while h == 1:   
            # Allow the player to take their turn
            player_hand = player_turn(dealer_hand)
            
            # Check if the player has a blackjack
            if hand_value(player_hand) == 21:
                print("\nYou have a blackjack!")
            
            # Allow the dealer to take their turn
            dealer_turn(dealer_hand)
            
            # Check if the dealer has a blackjack
            if hand_value(dealer_hand) == 21:
                print("\nDealer has blackjack!")
            
            # Determine the value of the player's and dealer's hands
            player_value = hand_value(player_hand)
            dealer_value = hand_value(dealer_hand)
            
            # Check who won the game
            if dealer_value > 21:
                print("\nDealer busts! You win!")
            elif dealer_value > player_value:
                print("\nDealer wins!")
            elif dealer_value < player_value:
                print("\nYou win!")
            else:
                print("\nIt's a tie!")
            break
        
        time.sleep(1)
        
        # Ask the player if they want to play again
        play_again = input("\nDo you want to play again? (Y/N) ").lower()
        
        # If the player wants to play again, restart the game
        if play_again == "y":
            main()

        # Otherwise, end the game and exit the program
        else:
            print("\nThanks for playing!\n\n")
            time.sleep(1)
            exit()

    # Call the main function if this script is run as the main program
    if __name__ == "__main__":
        main()

# multiplayer
elif game_mode == "2":

    # Define the multiplayer animation sequence
    animation = ["Starting Multiplayer game.","Starting Multiplayer game..", "Starting Multiplayer game..."]

    # Print the animation sequence
    print("\n\n")

    for i in range(len(animation)):
        time.sleep(0.6)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    time.sleep(1)
    print("\n")

    # Print a welcome message
    print("\nWelcome to  Multiplayer Blackjack!\n\n")
    time.sleep(1)

    # Define the deck of cards for multiplayer mode
    deck = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    deck *= 4


    # takes a number of cards to deal and returns a list of strings representing the cards
    def deal_cards(num_cards):
        time.sleep(0.5)
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

        for _ in range(num_aces):
            value += 11 if value <= 10 else 1
        return value

    # takes a list of cards and displays them on the screen
    def display_hand(hand, player_name=None, above=False, is_dealer=False, show_all=True):

        # If above and is_dealer are True, display "Dealer's hand"
        if above and is_dealer:
            print("Dealer's hand: ", end="")

        # If player_name is not None, display "{player_name}'s hand"
        if player_name:
            for card in hand:
                print(f"{str(card)} ", end="")
            print(f"({hand_value(hand)})")

        # If above and is_dealer are False and show_all is True, display all cards in the hand
        elif not above and not is_dealer:
            for i, card in enumerate(hand):
                if i == 0 and show_all or i != 0:
                    print(f"{str(card)} ", end="")
                else:
                    print("[hidden] ", end="")
            print(f"({hand_value(hand)})")

        # If above is False and is_dealer is True, display only the first card in the dealer's hand
        elif not above:
            print("\nDealer's hand: ", end="")
            print("[hidden] " if show_all else f"{str(hand[0])} ", end="")
            print(f"({hand_value([hand[0]])})", end="")

        # If above is True, display all cards in the hand except the first one
        else:
            for i, card in enumerate(hand):
                if i == 0 and above or i != 0 or show_all:
                    print(f"{str(card)} ", end="")
                else:
                    print("[hidden] ", end="")

            # If above and show_all are False, display the first card as hidden
            if not above and not show_all:
                print("[hidden] ", end="")
            print(f"({hand_value(hand)})")
    
    # represents the player 1's turn in the game
    def player_turn_1(player1_hand, dealer_hand):

        # deal two cards to player1
        player1_hand = deal_cards(2)

        # Display the dealer's first card and hide the second one
        print("\n\nDealer's hand:")
        print(f"{str(dealer_hand[0])} [hidden] ", end="")
        time.sleep(.5)

        # Display the player1's hand
        print("\n\nPlayer 1's hand:", "\n", end=' ')
        display_hand(player1_hand, player_name="Player 1", is_dealer=False, above=True, show_all=True)
        time.sleep(.5)

        # Keep asking player1 if they want to hit or stand until they stand or bust
        while True:

            # Check if player1 busts
            if hand_value(player1_hand) > 21:
                print("Bust! Player 1 loses.")
                time.sleep(1)
                return []
            
            # Asks player1 if they want to hit or stand
            time.sleep(.5)
            choice = input("\nPlayer 1, do you want to (h)it or (s)tand? ")

            # If player1 chooses to hit, deal another card and display the hand
            if choice.lower() in ['hit', 'h']:
                player1_hand += deal_cards(1)
                print("\nPlayer 1's hand:", "\n", end=' ')
                display_hand(player1_hand, player_name="Player 1", is_dealer=False, above=True, show_all=True)

            # If player1 chooses to stand, display the final hand and exit the loop
            elif choice.lower() in ['stand', 's']:
                print("\nPlayer 1's final hand:", end=' ')
                display_hand(player1_hand, player_name="Player 1", is_dealer=False)
                break

            # If player1 enters an invalid input, display an error message and exit the program
            else:
                print("Error. Please hit or stand.\n\n")
                time.sleep(1)
                exit()
                
        return player1_hand
    
    # represents the player 2's turn in the game
    def player_turn_2(player2_hand, dealer_hand):

        # deal two cards to player2
        player2_hand = deal_cards(2)

        # Display the dealer's first card and hide the second one
        print("\n\nDealer's hand:")
        print(f"{str(dealer_hand[0])} [hidden] ", end="")
        time.sleep(.5)

        # Display player2's hand
        print("\n\nPlayer 2's hand:", "\n", end=' ')
        display_hand(player2_hand, player_name="Player 2", is_dealer=False, above=True, show_all=True)
        time.sleep(.5)

        # Keep asking player2 if they want to hit or stand until they stand or bust
        while True:

            # Check if player2 busts
            if hand_value(player2_hand) > 21:
                print("Bust! Player 2 loses.")
                time.sleep(1)
                return []
            
            # Asks player2 if they want to hit or stand
            time.sleep(.5)
            choice = input("\nPlayer 2, do you want to (h)it or (s)tand? ")

            # If player2 chooses to hit, deal another card and display the hand
            if choice.lower() in ['hit', 'h']:
                player2_hand += deal_cards(1)
                print("\nPlayer 2's hand:", "\n", end=' ')
                display_hand(player2_hand, player_name="Player 2", is_dealer=False, above=True, show_all=True)

            # If player2 chooses to stand, display the final hand and exit the loop
            elif choice.lower() in ['stand', 's']:
                print("\nPlayer 2's final hand:", end=' ')
                display_hand(player2_hand, player_name="Player 2", is_dealer=False)
                break

            # If player2 enters an invalid input, display an error message and exit the program
            else:
                print("Error. Please hit or stand.\n\n")
                time.sleep(1)
                exit()

        return player2_hand
    
    # represents the dealer's turn in the game
    def dealer_turn(dealer_hand):

        # display the dealer's hand
        print("\n\nDealer's hand:")
        display_hand(dealer_hand)
        time.sleep(.5)
    
        # The dealer hits as long as the hand value is less than 17
        while hand_value(dealer_hand) < 17:
            dealer_hand += deal_cards(1)
            print("\nDealer hits:\n")
            display_hand(dealer_hand)
            print("\n")
            time.sleep(1)

    # deals two cards to both the player's and the dealer and returns the dealer's hand and the player's hand's
    def deal_initial_hands():
        dealer_hand = deal_cards(2)
        player1_hand = deal_cards(2)
        player2_hand = deal_cards(2)
        return dealer_hand, player1_hand, player2_hand
    
    # determins the winner of the game in every possibe outcome
    def determine_winner(player1_hand, player2_hand, dealer_hand):

        # Get the hand value for each player and the dealer.
        player1_value = hand_value(player1_hand)
        player2_value = hand_value(player2_hand)
        dealer_value = hand_value(dealer_hand)

        # Determine the winner based on the hand values.
        if player1_value > 21:
            if player2_value > 21:
                print("\nBoth players bust! Dealer wins!")
            else:
                print("\nPlayer 1 busts! Player 2 wins!")
        elif player2_value > 21:
            print("\nPlayer 2 busts! Player 1 wins!")
        elif dealer_value > 21:
            if player1_value == player2_value:
                print("\nBoth players win! Dealer busts!")
            elif player1_value > player2_value:
                print("\nPlayer 1 wins! Both players beat the dealer!")
            else:
                print("\nPlayer 2 wins! Both players beat the dealer!")
        elif dealer_value == player1_value == player2_value:
            print("\nIt's a three-way tie!")
        elif dealer_value == player1_value:
            if dealer_value > player2_value:
                print("\nDealer and Player 1 tie! Dealer wins against Player 2!")
            elif dealer_value < player2_value:
                print("\nDealer and Player 2 tie! Player 2 wins against Player 1!")
        elif dealer_value == player2_value:
            if dealer_value > player1_value:
                print("\nDealer and Player 2 tie! Dealer wins against Player 1!")
            elif dealer_value < player1_value:
                print("\nDealer and Player 1 tie! Player 1 wins against Player 2!")
        elif player1_value == player2_value:
            if player1_value > dealer_value:
                print("\nBoth players win against Dealer!")
            else:
                print("\nDealer wins against both players!")
        elif dealer_value > player1_value and dealer_value > player2_value:
            print("\nDealer wins against both players!")
        elif player1_value > dealer_value and player1_value > player2_value:
            print("\nPlayer 1 wins!")
        elif player2_value > dealer_value and player2_value > player1_value:
            print("\nPlayer 2 wins!")
        else:
            print("\nIt's a tie!")

        return determine_winner
    
    # This function is the main program that runs the game
    def main(): 

        # Deal the initial hands to the dealer and player
        player1_hand, player2_hand, dealer_hand = deal_initial_hands()

        # Player and dealer turns
        player_turn_1(player1_hand, dealer_hand)
        player_turn_2(player2_hand, dealer_hand)
        dealer_turn(dealer_hand)
        determine_winner(player1_hand, player2_hand, dealer_hand)

        time.sleep(1)

        # Ask the player if they want to play again
        play_again = input("\nDo you want to play again? (Y/N) ").lower()

        # If the player wants to play again, restart the game
        if play_again == "y":
            main()

        # Otherwise, end the game and exit the program
        else:
            print("\nThanks for playing!\n\n")
            time.sleep(3)
            exit()

    # Call the main function if this script is run as the main program
    if __name__ == "__main__":
        main()

# autonomous
elif game_mode == "3":

    # Define the autonomous animation sequence
    animation = ["Starting Autonomous game.","Starting Autonomous game..", "Starting Autonomous game..."]

    # Print the animation sequence
    print("\n\n")

    for i in range(len(animation)):
        time.sleep(0.6)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    time.sleep(1)
    print("\n")

    # Print a welcome message
    print("\nWelcome to  Autonomous Blackjack!\n\n")
    time.sleep(1)

    # Define the deck of cards for autonomous mode
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

        for _ in range(num_aces):
            value += 11 if value <= 10 else 1
        return value
    
    # represents the autoplayer's turn in the game
    def autoplayer_turn(player_hand, player_stand):
        
        # Loop until a condition is met
        while True:
            # If player busts, return 22
            if hand_value(player_hand) > 21:
                return [22]
            # If player's hand >= their stand value, exit the loop
            if hand_value(player_hand) >= player_stand:
                break
            # If player's hand < their stand value, deal another card and continue loop
            else:
                player_hand += deal_cards(1)

        # Return the player's hand
        return player_hand
    
    # represents the autodealer's turn in the game
    def autodealer_turn(dealer_hand,):

        # Deal cards to the dealer until their hand value is at least 17
        while hand_value(dealer_hand) < 17:
            dealer_hand += deal_cards(1)

        # Return the dealer's final hand
        return dealer_hand

    # determines the winner
    def determine_winner(player_hand, dealer_hand):

        # Calculate the total value of the player's hand and dealer's hand
        player_total = hand_value(player_hand)
        dealer_total = hand_value(dealer_hand)

        # Determine the winner based on the rules of blackjack
        if (player_total > 21 
            or dealer_total <= 21 
            and player_total <= dealer_total 
            and dealer_total > player_total
        ):
            return "Dealer"
        elif dealer_total > 21 or player_total > dealer_total:
            return "Player"
        else:
            return "Tie"

    # deals two cards to both the autoplayer and the autodealer and returns the autodealer's hand and the autoplayer's hand
    def deal_initial_hands():
        dealer_hand = deal_cards(2)
        player_hand = deal_cards(2)
        return dealer_hand, player_hand
    
    # This function is the main program that runs the game
    def main():

        # Get the number of games to play from user input, check if input is valid
        num_games_str = input("\n\nHow many games would you like to play? ")

        # If input is invalid, print error message and exit
        if not num_games_str.isdigit():
            time.sleep(0.5)
            print("Error. Please hit or stand.\n\n")
            time.sleep(1)
            exit()
        else:
            num_games = int(num_games_str)
            time.sleep(0.5)


        # Get the value at which the player should hold from user input, check if input is valid
        global player_stand
        player_stand_str = input("\nAt what value would you like for the player to hold? ")

        # If input is invalid, print error message and exit
        if not player_stand_str.isdigit():
            time.sleep(0.5)
            print("Error. Please enter a valid integer.\n\n")
            time.sleep(1)
            exit()
        else:
            player_stand = int(player_stand_str)
        
        
        # Create an animation to display while the simulation loads
        animation = ["Loading Simulation ⢿ ", "Loading Simulation ⣻ ", "Loading Simulation ⣽ ", "Loading Simulation ⣾ ",
                    "Loading Simulation ⣷ ", "Loading Simulation ⣯ ", "Loading Simulation ⣟ ", "Loading Simulation ⡿ ", 
                    "Loading Simulation ⢿ ", "Loading Simulation ⣻ ", "Loading Simulation ⣽ ", "Loading Simulation ⣾ ",
                    "Loading Simulation ⣷ ", "Loading Simulation ⣯ ", "Loading Simulation ⣟ ", "Loading Simulation ⡿ ", ]
        
        # Display the animation
        print("\n\n")

        for i in range(len(animation)):
            time.sleep(.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        

        console = Console()
        games = [f"game {n}" for n in range(num_games)]
        num_completed = 0

        print("\n")

        with console.status("[bold green]Simulating...") as status:
            while games:
                game = games.pop(0)
                time.sleep(0.001)
                num_completed += 1
                if num_completed % 100 == 0:
                    console.log(f"{num_completed} games completed")


        time.sleep(1)
        print("\n")

    
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
                    player_wins_game = True
                    player_wins += 1
                elif winner == "Dealer":
                    dealer_wins_game = True
                    dealer_wins += 1
                else:
                    tie_game = True
                    ties += 1

    
                # Print game results
                writer.writerow([game+1, dealer_wins_game, player_wins_game, tie_game, dealer_bj_game, player_bj_game, not(dealer_bj_game or player_bj_game)])

                num_no_blackjack = int(num_games) - (int(dealer_bj) + int(player_bj))
                total_bj = int(dealer_bj) + int(player_bj)

            animation = ["    Final Results    ", "  - Final Results -   ", "--- Final Results --- "]

            print("\n\n")

            for i in range(len(animation)):
                time.sleep(.4)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            time.sleep(1)
            print("\n")

            print(f"Player Stand: {player_stand}")
            print(f"Player Wins: {player_wins}")
            print(f"Dealer Wins: {dealer_wins}")
            print(f"Ties: {ties}")
            print(f"Total Blackjacks: {total_bj}")
            print("Check .csv for more info. More info displayed on graphs.")

            time.sleep(1)

            # Create the first pie chart
            y = np.array([dealer_bj, player_bj, num_no_blackjack])
            ylabels = ["Dealer Blackjacks", "Player Blackjacks", "No Blackjacks"]
            explode = (0.05, 0.05, 0)

            fig, ax = plt.subplots()
            plt.pie(y, labels = ylabels, explode=explode, autopct='%1.1f%%', textprops={'fontsize': 8, 'weight':'bold'}, radius=.7, startangle=90, colors=['black', 'red', 'green'])
            ax.legend(ylabels, title="Legend", loc="center right", bbox_to_anchor=(0.8, 0, 0.5, 1))
            fig.set_facecolor('#4f4f4f')
            ax.set_title('Chances of a Blackjack', fontweight = 'bold')

            for text in ax.texts:
                text.set_color('yellow')

            plt.savefig('ChanceOfBlackjack.png')

            # Create the second pie chart
            z = np.array([player_wins, dealer_wins, ties])
            zlabels = ["Wins", "Losses", "Ties"]
            explode = (0, 0, 0)

            fig, ax = plt.subplots()
            plt.pie(z, labels = zlabels, explode=explode, autopct='%1.1f%%', textprops={'fontsize': 8, 'weight':'bold'}, radius=.7, startangle=90, colors=['blue', 'red', 'yellow'])
            ax.legend(zlabels, title="Legend", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 1))
            fig.set_facecolor('#4f4f4f')
            ax.set_title('Chances of Winning', fontweight = 'bold')

            for text in ax.texts:
                text.set_color('black')

            plt.savefig('ChanceOfWin.png')

            # Ask the user if they want to view the graphs now
            answer = input("\nDo you want to view the graphs now? (y/n): ")
            time.sleep(.4)

            if answer.lower() == "y":
                # Show the saved images
                Image.open('ChanceOfBlackjack.png').show()
                Image.open('ChanceOfWin.png').show()
            else:
                print("\nGraphs saved to current working directory:")

            # Show the current working directory
            print(" -> ", os.getcwd())


            animation = ["        DONE        ", "      - DONE -      ", "     -- DONE --     ",
                         "    --- DONE ---    ", "   ---- DONE ----   ", "  ----- DONE -----  "
                         ," ------ DONE ------ ", "------- DONE -------"]

            print("\n")

            for i in range(len(animation)):
                time.sleep(.4)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()

            time.sleep(1)
            print("\n")

    # Call the main function if this script is run as the main program
    if __name__ == "__main__":
        main()

# Invalid Input
else:
    
    print("Error. Please enter 1, 2, or 3.\n\n")
    time.sleep(1)


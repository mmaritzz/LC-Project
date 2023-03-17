# LC-Project



### Demo of graphs:

RESULTS: 10000 GAMES
 
<img src="https://user-images.githubusercontent.com/118645227/225812695-2ce5db47-0029-4176-9e9c-22a4f634c3c5.png" width="410"> <img src="https://user-images.githubusercontent.com/118645227/225812768-b107478f-6e8b-453c-938d-1babfa5f03f4.png" width="410">










## Blackjack
### LCCS Project Write up 2022/23

Exam Number: 140802

### 1. Meeting the Brief (max 500 words): 250

For this project, I created a computer model of a simple blackjack game that meets the requirements outlined in the overview. Users can interact with models and play games. This includes some degree of randomness to ensure different behaviour each time it is run. The game accepts at least three different inputs, and all data are validated against the appropriate validation rules. You can play in Singleplayer, Multiplayer or Autonomous mode. Beyond meeting the basic requirements, we extended the model to store outcome data for each game played (wins, losses, draws, number of blackjacks in each session, etc.) in a file or database. We have also developed algorithms that perform statistical analysis, calculate average probabilities of blackjack, winning, losing or tying, and effectively communicate the resulting information in graphical form. This model was also used to test hypotheses such as when the dealer must take the position of 18+ or 16+. By changing the game's rules, you can show how the outcome and odds of winning are affected. This project allows users to enjoy a simple blackjack game, analyze game statistics, and test different scenarios to gain a deeper understanding of the game. Overall, this project is all about briefing: creating an interactive computer model of the game, validating input data, providing multiple game modes, storing and analyzing result data, and testing hypotheses to gain game insights. Meet the requirements. This balanced project provides users with a fun and immersive gaming experience while providing analytical tools to understand game statistics.

### 2. Investigation and Plan (approximately 400 words): 338

When I started working on the project, I wanted to create something challenging and extend my programming skills. After some research, the idea soon came to me to create a simple blackjack game. With some randomness, input validation required, and the ability to build in different modes, it was the perfect project for me. However, I quickly realized that I needed to remember more of what I had learned about programming in Python, as I had forgotten a lot and had a hard time starting the project. I faced a steep learning curve and knowing where to start working. However, I did not let it discourage me. I threw myself first into the project and built the structure from what I had built. When I started working on games, I noticed my programming skills slowly returning. It was a slow process at first, but as I worked on the project, I began to recall various programming concepts and techniques I had previously learned. I started getting comfortable with the code and was able to progress faster. One of the biggest challenges I faced was creating the game's structure. I had to figure out how to store the data for each player, deck, and game rules. It was tough, but I was determined to do it. I have spent hours writing, debugging, and testing code to ensure it works correctly. I had some difficulties at first, but in the end, I was able to create a working version of the game. Seeing my hard work pay off was exhilarating and motivated me to keep improving the game. Added new features such as the ability to save the results of each game played and performed statistical analysis of the data. Overall, the experience of working on this project has been rewarding but enriching. I learned a lot about programming in Python and created something I am proud of. Thanks to this project, I took a step forward in my programming journey. I want to keep learning and improving my skills.

### 3. Design (approximately 400 words): 341

I only did a little investigating to begin this project. I only really researched the proper rules of blackjack, so I had that basic understanding of how this project should act. When designing this project, I needed a plan, but I did not have one. I went head first, so I was surprised that I could produce something that is 1. easy to read and 2. easy to use. Overall I am happy with how it came out. I made three separate .py files, single player, multiplayer and autonomous. Single-player was easy to do. It took me less than a week. It took me about a week to decide how I wanted it to print in the console and how it would look for the user. The Multiplayer mode took so much longer than it should have. I cannot tell you why it took me 2-3 weeks to get working. I did not like this part of the project. Error after error, I felt like I was going clinically insane. Autonomous was a breeze, and it took me an afternoon to complete. After this, I made a simple user interface so the user could pick between modes, and this was the basic requirements finished. My next step was configuring the CSV element and getting that to work and look nice. I wanted the stats to portray a specific way, which has been achieved—following step, graphs. I did the charts in a day, and I had never used them like this before, so it was a fun learning experience. I think they look very nice for what tools I had. Overall I feel like I did very well with my knowledge and ability in python. I liked jumping straight into the project without a plan as I got to brainstorm on the spot, critically thinking throughout, thinking of an idea and sticking to it, only branching off and improving it more and more. I enjoyed this. I do not see any improvements I could make other than more validation and error handling.

### 4. Implementation (approximately 500 words): 462

This code implements a simple text-based version of the game Blackjack. The game logic is implemented through a series of functions that interact with each other to run the game.
- 'deal_cards(num_cards)' is a function that takes several cards as an argument and returns a list of randomly selected cards from a predefined deck list. Each card is converted to a string representation before being added to the list. 
- 'hand_value(hand)' is a function that takes a hand of cards as an argument and calculates the hand's value for the game of Blackjack. It iterates through each card in hand, adding 10 for face cards (J, Q, K), keeping track of the number of Aces in hand, and adding the numerical value of each non-face card. It then iterates through the number of Aces and adds 1 or 11 to the total value, depending on which value would be more advantageous for the player.
- 'display_hand(hand, player_name=None, above=False, is_dealer=False, show_all=True)' is a function that takes a hand of cards as an argument, along with several optional arguments determining how the hand should be displayed. If 'player_name' is provided, it will print the player's name and the value of their hand. If 'above' is True, it will print the first card in hand above the other cards. If 'is_dealer' is True, it will print "Dealer's hand" instead of the player's name. If 'show_all' is False, it will hide all but the first card in hand.
- 'deal_initial_hands()' This function deals two cards to the player and the dealer, returning their hands as separate lists.
- 'main()' This function is the primary driver of the program. It is slightly different for each mode. It welcomes the player to the game of Blackjack and deals the initial hands. It then allows the players to take their turn and the dealer to take their turns, displaying the game's outcome. It then prompts the player to play again or exit the game. If the player chooses to play again, the main() function is called recursively. In autonomous, it only shows who wins the game, and after a certain amount of play, user-defined, it logs information such as wins, losses, ties, total blackjacks, etc. This information is logged into a .csv file. 2 pie charts are also produced showing wins, losses, and ties; the other shows player blackjack percentage, dealer blackjack percentage, and percentage of no blackjack.
Since many functions are being reused, it may become apparent that it will be easier to include no duplicate functions and call them when needed. However, while coding this, I broke the project into three projects, singleplayer, multiplayer, and autonomous. Doing this was easiest, making it easier to understand how each mode works as all the code for it is together.

### 5.  Testing (approximately 350 words): 291 

Troubleshooting this project was smooth. If I got an error, I either knew how to fix it, or I could google a fix, or if I needed to learn how to do something correctly, I would look it up on w3schools or other resources. The hardest part of this code was getting the multiplayer aspect to work. I could not tell you why, but I kept slipping up, then I would fix that issue, and another would arise. I did not like this point in the code. One night, everything just worked, and I was overjoyed. I put all the projects into a final project, and everything was fine and dandy. Troubleshooting the autonomous was rough, but it evened out quickly. Mainly because I wanted it to show a specific way, once I got that down, I added .csv capabilities. This process started off rough, but I nailed it in the end. I am thrilled with how the information comes out on the CSV file. I did the graphs in a couple of hours. I am saddened that there is a lot you can do to make the pie charts look good, but I will take how they look. It is easy to read and portrayed in a visually pleasing manner. Implementing and testing my hypothesis was interesting. I thought about changing the dealer's stand value, but I soon realized there is no practical use for this as you cannot change the dealer's stand value in standard blackjack, so what if the player stood on a specific number or higher? What kind of results could this give off? can it give an optimal strategy for winning? I believe this is more practical and knowledgeable as its a viable and legal strategy




REFERENCES:

- https://code.visualstudio.com/docs/python/python-tutorial
- https://www.w3schools.com/python/python_pip.asp
- https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- https://www.w3schools.com/python/python_file_write.asp
- https://www.w3schools.com/python/python_try_except.asp
- https://github.com/sepandhaghighi/art#usage
- https://www.w3schools.com/python/python_variables_global.asp
- https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
- https://pythonguides.com/matplotlib-title-font-size/


 


# LC-Project



 Demo of graphs:

 RESULTS: 10000 GAMES (csv included with files)
 
![image](https://user-images.githubusercontent.com/118645227/225509523-d28f2c7a-9c82-4ff9-bca9-840acd453cbc.png | width=400)

![image](https://user-images.githubusercontent.com/118645227/225509556-66d66cd0-c322-484a-9a6e-0b5f7f87a518.png | width=400)








Blackjack
LCCS Project Write up 2022/23

Exam Number: 140802
1. Meeting the Brief (max 500 words):

For this project, I created a computer model of a simple blackjack game that meets the requirements outlined in the overview. Users can interact with models and play games. This includes some degree of randomness to ensure different behavior each time it is run. The game accepts at least three different inputs and all data are validated against the appropriate validation rules. You can play in Singleplayer, Multiplayer or Autonomous mode. Beyond meeting the basic requirements, we extended the model to store outcome data for each game played (wins, losses, draws, number of blackjacks in each session, etc.) in a file or database. We have also developed algorithms that perform statistical analysis, calculate average probabilities of blackjack, winning, losing or tying, and effectively communicate the resulting information in graphical form. Additionally, this model was used to test hypotheses such as when the dealer must take the position of 18+ or 16+. By changing the rules of the game, you can show how the outcome and odds of winning are affected. This project allows users to not only enjoy a simple blackjack game, but also analyze game statistics and test different scenarios to gain a deeper understanding of the game. Overall, this project is all about briefing: creating an interactive computer model of the game, validating input data, providing multiple game modes, storing and analyzing result data, and testing hypotheses to gain game insights. meet the requirements. This is a balanced project that provides users with a fun and immersive gaming experience while providing analytical tools to understand game statistics.

2. Investigation and Plan (approximately 400 words):

When I started working on the project, I wanted to create something that would challenge me and extend my programming skills. After some research, the idea soon came to me to create a simple blackjack game. With some randomness, input validation required, and the ability to build in different modes, it seemed like the perfect project for me. However, I quickly realized that I had forgotten a lot of what I had learned about programming in Python, and I had a hard time starting the project at first. I faced a steep learning curve and it was difficult to know where to start. But I didn't let it discourage me. I decided to throw myself first into the project and build the structure out of what I had built. When I started working on games, I noticed my programming skills slowly coming back. It was a slow process at first, but as I worked on the project, I began to recall various programming concepts and techniques that I had previously learned. I started getting comfortable with the code and was able to progress faster. One of the biggest challenges I faced was creating the structure of the game. I had to figure out a way to store the data for each player, deck, and game rules. It was tough, but I was determined to do it. I've spent hours writing, debugging, and testing code to make sure it's working correctly. I had some difficulties at first, but in the end I was able to create a working version of the game. Seeing my hard work pay off was exhilarating and gave me the motivation to keep improving the game. Added new features such as the ability to save the results of each game played and perform statistical analysis of the data. Overall, the experience of working on this project has been rewarding, but incredibly rewarding. I learned a lot about programming in Python and was able to create something I'm proud of. Thanks to this project, I was able to take a step forward in my programming journey. I want to keep learning and improve my skills.

3. Design (approximately 400 words):

I only did a little investigating to begin this project. I only really researched the proper rules of blackjack, so I had that basic understanding of how this project should act. When designing this project, I needed a plan to begin with, but I didn't have one. I went head first, so I was surprised that I could produce something that is 1. easy to read and 2. easy to use. Overall I am happy with how it came out. I made three separate .py files, single player, multiplayer and autonomous. Single-player was easy to do. It took me less than a week. It took me about a week to decide how I wanted it to print in the console and how it would look for the user. The Multiplayer mode took so much longer than it should have. I cannot tell you why it took me 2-3 weeks to get working. I wouldn't say I liked this part of the project. Error after error, I felt like I was going clinically insane. Autonomous was a breeze, and it took me an afternoon to complete. After this, I made a simple user interface so the user could pick between modes, and this was the basic requirements finished. My next step was configuring the csv element and getting that to work and look nice. I wanted the stats to portray a specific way, and this has been achieved—next step graphs. I did the charts in a day, and I had never used them like this before, so it was a fun learning experience. I think they look very nice for what tools I had. Overall I feel like I did very well with my knowledge and ability in python. I really liked jumping straight into the project without a plan as I got to brainstorm on the spot, critically thinking throughout, thinking of an idea and sticking to it, only branching off of it and improving it more and more. I really enjoyed this. I don't see any improvements that I could make other than more validation and error handling.

4. Implementation (approximately 500 words):

This code implements a simple text-based version of the game Blackjack. The game logic is implemented through a series of functions that interact with each other to run the game.
- 'deal_cards(num_cards)' is a function that takes several cards as an argument and returns a list of randomly selected cards from a predefined deck list. Each card is converted to a string representation before being added to the list. 
- 'hand_value(hand)' is a function that takes a hand of cards as an argument and calculates the hand's value for the game of Blackjack. It iterates through each card in hand, adding 10 for face cards (J, Q, K), keeping track of the number of Aces in hand, and adding the numerical value of each non-face card. It then iterates through the number of Aces and adds 1 or 11 to the total value, depending on which value would be more advantageous for the player.
- 'display_hand(hand, player_name=None, above=False, is_dealer=False, show_all=True)' is a function that takes a hand of cards as an argument, along with several optional arguments determining how the hand should be displayed. If 'player_name' is provided, it will print the player's name and the value of their hand. If 'above' is True, it will print the first card in hand above the other cards. If 'is_dealer' is True, it will print "Dealer's hand" instead of the player's name. If 'show_all' is False, it will hide all but the first card in hand.
- 'deal_initial_hands()' This function deals two cards to the player and the dealer, returning their hands as separate lists.
- 'main()' This function is the primary driver of the program. It is slightly different for each mode. It welcomes the player to the game of Blackjack and deals the initial hands. It then allows the players to take their turn and the dealer to take their turns, displaying the game's outcome. It then prompts the player to play again or exit the game. If the player chooses to play again, the main() function is called recursively. In autonomous, it only shows who wins the game, and after a certain amount of play, user-defined, it logs information such as wins, losses, ties, total blackjacks, etc. This information is logged into a .csv file. 2 pie charts are also produced showing wins, losses, and ties, and the other shows player blackjack percentage, dealer blackjack percentage, and percentage of no blackjack.
Since many functions are being reused, it may become apparent that it will be easier to include no duplicate functions and call them when needed. However, while coding this, I broke the project down into three projects, singleplayer, multiplayer, and autonomous. Doing this was easiest, in my opinion, and it makes it easier to understand how each mode works as all the code for it is right there together.

5.  Testing (approximately 350 words):

Troubleshooting this project wasn't a headache at all. I felt like if I got an error, I either knew how to fix it, or I could google a fix, or if I never knew how to do something properly, I would look it up on w3schools or other resources. The hardest part of this code was getting the multiplayer aspect to work. I couldn't tell you why, but I kept on slipping up, then I would fix that issue, then another would arise. I wouldn't say I liked this point in the code. One night, everything just worked, and I was overjoyed. I put all the projects into a final project, and everything was fine and dandy. troubleshooting the autonomous was rough, to begin with, but it evened out pretty quickly. Mainly because I wanted it to show a specific way. Once I got that down, I added .csv capabilities. This started off rough but nailed it in the end. I'm thrilled with how the information comes out on the csv file. I did the graphs in a couple of hours. I'm saddened that there is a lot you can do to make the pie charts look good, but I'll take how they look. it is easy to read and portrayed in a visually pleasing manner.




REFERENCES:
- https://code.visualstudio.com/docs/python/python-tutorial
- https://www.w3schools.com/python/python_pip.asp
- https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://www.w3schools.com/python/python_file_write.asp
- https://www.w3schools.com/python/python_try_except.asp

 


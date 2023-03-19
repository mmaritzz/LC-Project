# LCCS-Project


## ***Write up is below the graphs.***

### Demo of graphs:

RESULTS: 10000 GAMES
 
<img src="https://user-images.githubusercontent.com/118645227/225812695-2ce5db47-0029-4176-9e9c-22a4f634c3c5.png" width="410"> <img src="https://user-images.githubusercontent.com/118645227/225812768-b107478f-6e8b-453c-938d-1babfa5f03f4.png" width="410">


****

## LCCS Project Write up 2022/23
### Blackjack

Exam Number: 140802

### 1. Meeting the Brief (max 500 words): 253

I successfully met the requirements of this project by creating a computer model of the popular card game blackjack. This meets the first, second, and third basic requirements. The three inputs include the player's bet, the player's choice to hit or stand, and the number of decks used in the game. All input data is validated to ensure the user inputs correct and valid information.

 The game has three modes, including single-player, multi-player, and autonomous. The user can choose to play alone or against other players and simulate different scenarios to improve their gameplay. In addition to the basic requirements, I have also fulfilled the advanced requirements of the project. Firstly, I have extended the basic model to store the results data from the game played in a CSV file. This includes storing wins, losses, draws, the number of blackjacks in each session, and other information. Secondly, I have made graphs based on the stored data, which show the probability of a blackjack between the dealer and player and another graph showing the win-loss-tie percentage of a game played. This allows the user to visualize and analyze game statistics.

 Lastly, I have used the model to test hypotheses. What is the optimal number of standing when playing blackjack? This provides a valuable tool for users to test different strategies and improve their gameplay. Overall, I am pleased with my project as it makes a blackjack game enjoyable and includes data storage, statistical analysis, and the ability to test hypotheses and make future predictions.


### 2. Investigation and Plan (approximately 400 words): 437

When I started working on the project, I wanted to create something challenging and extend my programming skills. After some research, the idea soon came to me to create a simple blackjack game. With some randomness, input validation required, and the ability to build in different modes, it was the perfect project for me. However, I quickly realized that I needed to remember more of what I had learned about programming in Python, and I had a hard time starting the project. I faced a steep learning curve, and it was not easy to know where to start.

Nevertheless, I did not let it discourage me. I threw myself first into the project and built the structure from what I had built. I abstracted a lot from traditional blackjack, but nearing the end, it could be an excellent tool for beginners who would like to pick up the basics and use the tools I provided. When I started working on the game, I noticed my programming skills slowly returning. It was a slow process at first, but as I worked on the project, I began to recall various programming concepts and techniques I had previously learned. I started getting comfortable with the code and was able to progress faster. One of the biggest 

challenges I faced was creating the game's structure, as I didn't-needed a specific plan, which I foolishly thought little of. In my own experience, this was not a challenge to begin with, and later on, when I incorporated GitHub, I uploaded any issues I had or anything I wanted to fix or change with my game. If I had made a visual of a plan or structure, this would have been so much more stress-free. I had to figure out how to store the data for each player, deck, and game rules. It was tough, but I was determined to do it. I have spent hours writing, debugging, and testing code to ensure it works correctly.
I had some difficulties at first, but in the end, I was able to create a working version of the game. Seeing my hard work pay off was exhilarating and motivated me to keep improving the game. Added new features such as the ability to save the results of each game played and performed statistical analysis of the data. Overall, the experience of working on this project has been rewarding but enriching. I learned a lot about programming in Python and created something I'm proud of. Thanks to this project, I took a step forward in my programming journey. I want to keep learning and improving my skills. 


### 3. Design (approximately 400 words): 437

I only did a little investigating to begin this project. I only really researched the proper rules of blackjack, so I had that basic understanding of how this project should act. I needed a plan when designing this project, but I did not have one. I went head first, so I was surprised that I could produce something that is 1. easy to read and 2. easy to use. Overall I am happy with how it came out. I made three separate .py files, single player, multiplayer and autonomous. Single-player was easy to do. It took me less than a week. It took me about a week to decide how I wanted it to print in the console and how it would look for the user. The Multiplayer mode took so much longer than it should have.

I cannot tell you why it took me 2-3 weeks to get working. I would not say I liked this part of the project. Error after error, I felt like I was going clinically insane. Autonomous was a breeze, and it took me an afternoon to complete. After this, I made a simple user interface so the user could pick between modes, and this was the basic requirements finished. My next step was configuring the CSV element and getting that to work and look nice. I wanted the stats to portray a specific way, which has been achieved—following step, graphs. I did the charts in a day, and I had never used them like this before, so it was a fun learning experience. I think they look very nice for what tools I had. Producing my flowchart was rough, to begin with, as I did not know how I was going to make one, but I found a helpful website, which I referenced, and I made the whole thing in about an hour and a half. On a basic level, it portrays how the code performs each task. I feel it does an excellent job of demonstrating that.

Overall I feel like I did very well with my knowledge and ability in python. I liked jumping straight into the project without a plan as I got to brainstorm on the spot, critically thinking throughout, thinking of an idea and sticking to it, only branching off and improving it more and more. I enjoyed this. I do not see any improvements I could make other than more validation and error handling.



### 4. Implementation (approximately 500 words): 462

This code implements a simple text-based version of the game Blackjack. The game logic is implemented through a series of functions that interact with each other to run the game.
'deal_cards(num_cards)' is a function that takes several cards as an argument and returns a list of randomly selected cards from a predefined deck list. Each card is converted to a string representation before being added to the list. 
'hand_value(hand)' is a function that takes a hand of cards as an argument and calculates the hand's value for the game of Blackjack. It iterates through each card in hand, adding 10 for face cards (J, Q, K), keeping track of the number of Aces in hand, and adding the numerical value of each non-face card. It then iterates through the number of Aces and adds 1 or 11 to the total value, depending on which value would be more advantageous for the player.
'display_hand(hand, player_name=None, above=False, is_dealer=False, show_all=True)' is a function that takes a hand of cards as an argument, along with several optional arguments determining how the hand should be displayed. If 'player_name' is provided, it will print the player's name and the value of their hand. If 'above' is True, it will print the first card in hand above the other cards. If 'is_dealer' is True, it will print "Dealer's hand" instead of the player's name. If 'show_all' is False, it will hide all but the first card in hand.
'deal_initial_hands()' This function deals two cards to the player and the dealer, returning their hands as separate lists.
'main()' This function is the primary driver of the program. It is slightly different for each mode. It welcomes the player to the game of Blackjack and deals the initial hands. It then allows the players to take their turn and the dealer to take their turns, displaying the game's outcome. It then prompts the player to play again or exit the game. If the player chooses to play again, the main() function is called recursively. In autonomous, it only shows who wins the game, and after a certain amount of play, user-defined, it logs information such as wins, losses, ties, total blackjacks, etc. This information is logged into a .csv file. 2 pie charts are also produced showing wins, losses, and ties; the other shows player blackjack percentage, dealer blackjack percentage, and percentage of no blackjack.
Since many functions are being reused, it may become apparent that it will be easier to include no duplicate functions and call them when needed. However, while coding this, I broke the project into three projects, singleplayer, multiplayer, and autonomous. Doing this was easiest, making it easier to understand how each mode works as all the code for it is together.


### 5.  Testing (approximately 350 words): 291 

Troubleshooting this project was a smooth process. If I got an error, I either knew how to fix it, or I could research a fix, or if I never knew how to do something correctly, I would look it up on w3schools or other resources. The hardest part of this code was getting the multiplayer aspect to work. I could not say why, but I kept slipping up, and then I would fix that issue, and another would arise. I did not like this point in the code.

 One night, everything just worked, and I was overjoyed. I put all the projects into a final project, and everything was fine and dandy. Troubleshooting the autonomous was rough, but it evened out quickly, mainly because I wanted it to show a specific way. Once I got that down, I added .csv capabilities. This started rough, but I nailed it in the end. I am thrilled with how the information comes out on the CSV file. I did the pie charts in a couple of hours. I am saddened that there is a lot you can do to make the pie charts look good, but I will take how they look. It is easy to read and portrayed in a visually pleasing manner. 

Each mode was made in its own unique file. I had a single-player .py, a multiplayer .py, an autonomous .py and a main .py. This was my instinct for some reason, and I think it was for good as I was able to perfect each mode to get them all working, then add them all to the main .py, and all I was left with was making everything look and feel nice, and that was it. Working throughout this project, a few of my friends and I discussed ideas and working strategies to benefit everyone in our little cliche. My family, friends and I did all the Alpha and Beta testing. I added any problems or changes I was recommended to my Git Repo as an issue, so I can go back to it and resolve it.


### 6. Evaluation (approximately 350 words): 0

This project came out nearly exactly how I planned it. I am thrilled with how it came out, and it feels complete to me, but I can definitely point out where it can be improved upon. 

For example, a limited number of decks could be used, which would require a new variable like "deck_num". By incorporating a "deck_num" variable, my project could become even more sophisticated and versatile. For example, I could develop different strategies for different numbers of decks, as the number of decks affects the odds of different cards being drawn. Additionally, I could consider incorporating other variables, such as a "true count" variable, which adjusts for the number of decks remaining in the dealer's shoe to improve the accuracy of the card counting algorithm. With these additional features, my tool could become a valuable resource for anyone looking to improve their blackjack skills. However, it is essential to note that while card counting is not illegal, casinos often frown upon it. They may take measures to prevent players from using these techniques. Therefore, it is essential to use this tool responsibly and in accordance with the rules of any particular casino or gambling establishment.

Another idea of improvement could be the implementation of Tkinter. I can make a friendly game interface and add card faces. It provides another way of identifying the cards and adds another element of realism, as it shows an actual card face rather than just a text representation. Tkinter would also include buttons and other interactive elements, which could make the game more engaging and intuitive for users. Furthermore, I could add sound effects and music to my game, enhancing the overall experience and creating a more immersive atmosphere. For example, I could include the sound of shuffling cards or the clinking of chips as they are placed on the table.

Additionally, I could incorporate background music that evokes the ambience of a real-life casino, such as jazz or lounge music. In terms of gameplay, I could also explore adding more variations to the basic rules of blackjack, such as splitting pairs or doubling down. These additional features would provide more opportunities for strategic decision-making and could make the game more challenging and exciting.

By incorporating these various improvements, I could create a more polished and engaging blackjack game that provides players with a more realistic and enjoyable experience.


### 7. References

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
- https://app.diagrams.net


8. Summary word count 


|Section | Word Count |
| --- | --- |
| 1. Meeting the Brief | 253 |
| 2. Investigation and Plan | 437 |
| 3. Design | 407 |
| 4. Implementation | 457 |
| 5. Testing | 348 |
| 6. Evaluation | 396 |
| **Total:** | 2298 |




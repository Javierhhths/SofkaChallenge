# SofkaChallenge: 25-Question Contest

# By: Javier Danilo Castro Faccetti

This contest was programmed in Python 3.7. It consists on three .py files: one containing the Game class, another one containing the QuestionRound class and, finally, the main one, in which anyone can execute the program. It also implements certain methods from the Pandas, Random and CSV libraries, to manipulate the input and output .csv files (question database and player history, respectively) and randomize the order of the questions.

# Instructions:

Rules: The contest consists of 5 rounds. Each round has 5 questions with 4 answer options (only one correct). You win the game if you answer correctly all 25 questions. Every 5 questions you also scale 1 round, being the first one the one with the lowest difficulty level and the fifth one the one with the most. You also get a prize money depending on the round you've just passed. If you answer wrongly any of the questions, you're out of the game inmediately with no prize. You can also retire and have the chance to take the money you've acumulated.

Input: The player name; A, B, C or D (answer options) or R (retirement). They can be either uppercase or lowercase.

Output: The player name, with the prize money, the question level and the round, and the prize money; all of these tabulated in the player history.

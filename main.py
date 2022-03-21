from Game import Game #Imports the Game class from its module
from QuestionRound import QuestionRound #Imports the QuestionRound class from its module
import csv
import pandas as pd

user=Game() #Instantiates the Game class
print(user.welcome_message)
name=user.NewPlayer()
for i in range(1,user.number_of_rounds+1,1): #Loops over the rounds of the contest and breaks in case the player either answers wrongly or retires
    rounds=QuestionRound()
    rounds.rand_question_round(i)
    if rounds.difficulty_level=="5th" and rounds.question_level=="5th":
        break
    elif rounds.answer==False:
        break
user.SavePlayer(name,rounds.question_level,rounds.difficulty_level,rounds.prize_money) #Saves player's data into the .csv output file
user.LoadPlayerHistory() #Shows player history
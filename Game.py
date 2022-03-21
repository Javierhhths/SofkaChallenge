from QuestionRound import QuestionRound #Imports the QuestionRound class from its module
import csv
import pandas as pd

class Game(): #This class instantiates the QuestionRound class in an attribute and specifies some methods to input a new player, save the player's data and keep a history of players and their levels, rounds and prize money reached; so it can be used correctly in the main.py with all its needed objects.
    
    def __init__(self):
        self.number_of_rounds=5
        self.round=1
        self.player_name=''
        self.new_round=QuestionRound()
        self.player_database='Player_History.csv' #Output rewritable .csv file with the players history
        self.welcome_message='\nHello! This is the 25-Step-Millionaire contest!\n\n\nYou are about to become rich. You just have to solve these 25 easy 4-option questions!'
        
    def NewPlayer(self):
        self.player_name=input("\nInput your name:\n\n")
        return self.player_name #Defines new players to the game
    
  
    def SavePlayer(self,name,question_level,round_number,prize): #Rewrites the 'Player_History.csv' file everytime main.py is run, with a row containing the last player's question level, round and prize money reached
        with open(r'Player_History.csv', 'a', newline='') as csvfile:
            fieldnames = ['NAME','QUESTION_LEVEL','ROUND','PRIZE_MONEY']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'NAME':name, 'QUESTION_LEVEL': question_level,'ROUND': round_number,'PRIZE_MONEY':prize})
        
    def LoadPlayerHistory(self): #Loads the player history file tabulated with the help of the read_csv Pandas' method
        return pd.read_csv(open('Player_History.csv'))


import pandas as pd
import csv
import random

class QuestionRound():#This class defines each round of questions of the game, loading the question database with Pandas and modifying the attributes of the round, depending on the user's performance

  def __init__(self):
        self.question_database=pd.DataFrame(data=pd.read_csv(open('Question_Database.csv')))
        self.number_of_questions=5
        self.prize_money=[20000,50000,100000,500000,1000000]
        self.question_level=["1st","2nd","3rd","4th","5th"]
        self.difficulty_level=["1st","2nd","3rd","4th","5th"]
        self.answer=True #This attribute uses boolean values depending on the answers (it is modified in case of retirement or wrong answers), so it could be easily taken in another class to continue or end the contest

  def rand_question_round(self,round): #Method that delivers all 5 questions of a round to the player. Returns the number of right answers, the level reached and the prize money
    indexes=list(self.question_database.loc[self.question_database["DIFFICULTY_LEVEL"]==round].index) #Determines the indexes of questions by level of difficulty
    random.shuffle(indexes)  #Randomizes the sequence of questions in the round
    count_ra=0 #Count of right answers
    while True:
      i=indexes[count_ra]
      try:
        answer=input('\n' + self.question_database["QUESTION"][i] + '\n\n' + self.question_database["OPTION_1"][i] + '\n' + self.question_database["OPTION_2"][i] + '\n' + self.question_database["OPTION_3"][i] + '\n' + self.question_database["OPTION_4"][i] + '\n\n' + 'Input either A, B, C or D. If you wanna retire now, input R.\n\n')
      except:
        print("\nYou can only input either A, B, C or D!")
      right_answer=str(self.question_database["ANSWER"][i])
      if answer.upper()==right_answer[0]:
        count_ra=count_ra+1
        if (count_ra==5 and round==1):
          print(f"\nCongratulations! You have moved on to the {self.difficulty_level[round]} round!")
          self.prize_money=self.prize_money[round-1]
          self.difficulty_level=self.difficulty_level[round-1]
          self.question_level="5th"
          break
        elif (count_ra==5 and round!=1 and round!=5):
          print(f"\nCongratulations! You have moved on to the {self.difficulty_level[round]} round!")
          self.prize_money=self.prize_money[round-2]
          self.difficulty_level=self.difficulty_level[round-1]
          self.question_level="5th"
          break
        elif (count_ra==5 and round==5):
          print("\nYou have won the game! Your final prize money is $1000000!")
          self.prize_money=self.prize_money[round-1]
          self.difficulty_level="5th"
          self.question_level="5th"
          break
        else:
          print(f"\nRight answer! You have moved on to the {self.question_level[count_ra]} level of the {self.difficulty_level[round-1]} round!")
          continue
      elif answer.upper()=='R':
        if count_ra==0 and round!=1:
          print(f"\nYou have retired. Your prize money is ${self.prize_money[round-2]} and your level is the {self.question_level[count_ra]} of the {self.difficulty_level[round-1]} round. Good luck for next time!\n")
          self.prize_money=self.prize_money[round-2]
          self.difficulty_level=self.difficulty_level[round-1]
          self.question_level=self.question_level[count_ra]
          self.answer=False
          break
        elif round==1:
          print(f"\nYou have retired. Your prize money is $0 and your level is the {self.question_level[count_ra]} of the {self.difficulty_level[round-1]} round. Good luck for next time!\n")
          self.prize_money=0
          self.difficulty_level=self.difficulty_level[round-1]
          self.question_level=self.question_level[count_ra]
          self.answer=False
          break
        else:
          print(f"\nYou have retired. Your prize money is ${self.prize_money[round-2]} and your level is the {self.question_level[count_ra]} of the {self.difficulty_level[round-1]} round. Good luck for next time!\n")
          self.prize_money=self.prize_money[round-2]
          self.difficulty_level=self.difficulty_level[round-1]
          self.question_level=self.question_level[count_ra]
          self.answer=False
          break
      elif ((answer.upper()!=right_answer[0]) and (answer.upper()=='A' or answer.upper()=='B' or answer.upper()=='C' or answer.upper()=='D')):
        if count_ra==0 and round!=1:
          print(f"\nWrong answer. Game over. Your prize money is ${self.prize_money[round-2]}. Good luck for next time!\n")
          self.prize_money=self.prize_money[round-2]
          self.difficulty_level=self.difficulty_level[round-1]
          self.question_level=self.question_level[count_ra]
          self.answer=False
          break
        elif round==1:
          print(f"\nWrong answer. Game over. Your prize money is $0 and your level is the {self.question_level[count_ra]} of the {self.difficulty_level[round-1]} round. Good luck for next time!\n")
          self.prize_money=0
          self.difficulty_level=self.difficulty_level[round-1]
          self.question_level=self.question_level[count_ra]
          self.answer=False
          break
        else:
          print(f"\nWrong answer. Game over. Your prize money is ${self.prize_money[round-2]} and your level is the {self.question_level[count_ra]} of the {self.difficulty_level[round-1]} round. Good luck for next time!\n")
          self.prize_money=self.prize_money[round-2]
          self.difficulty_level=self.difficulty_level[round-1]
          self.question_level=self.question_level[count_ra]
          self.answer=False
          break
      else:
        print("\nYou can only input either A, B, C or D!")
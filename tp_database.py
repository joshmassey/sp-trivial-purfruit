import pandas as pd
import csv
import os

class Database:

    def __init__(self):

        print('INIT DATABASE ACCESS')
        self.categories = {
                        'White': 'Events',
                        'Blue': 'Places',
                        'Green': 'Independence Day',
                        'Red': 'People'
                    }
        
        self.getQuestions()
        self.addQuestion()
        self.getQuestions()
        self.deleteQuestion()
        self.modifyQuestion()

    def addQuestion(self):

        print('Add new question to database')
        for key, value in self.categories.items():
            print('Color: {} / Category: {}'.format(key, value))
        self.color = input('Color category of new question: ')
        self.question = input('New question: ')
        self.answer = input('New answer: ')
        self.new_data = [self.color, self.categories[self.color], self.question, self.answer]
        self.new_df = pd.DataFrame([self.new_data], columns = ['color', 'category', 'question', 'answer'])
        self.df = pd.read_csv('./res/trivial_purfruit_questions.csv')
        self.df = self.df.append(self.new_df)
        self.df.to_csv('./res/trivial_purfruit_questions.csv', index = False)

    def deleteQuestion(self):

        self.getQuestions()
        self.delete_index = input('Enter index number to delete question: ')
        self.confirm = input('Confirm delete question at index ' + str(self.delete_index) + '? Confirm YES/NO: ')
        if self.confirm == 'YES':
            self.df = pd.read_csv('./res/trivial_purfruit_questions.csv')
            self.df = self.df.drop(int(self.delete_index))
            self.df.to_csv('./res/trivial_purfruit_questions.csv', index = False)
        elif self.confirm == 'NO':
            print('Cancel delete question')
        self.getQuestions()

    def modifyQuestion(self):

        self.getQuestions()
        self.df = pd.read_csv('./res/trivial_purfruit_questions.csv')
        self.select_index = input('Index of question to modify: ')
        self.change = input('Modify question or answer? (question/answer): ')
        self.new_content = input('Enter new content: ')
        print('Modify ' + self.change + ' at index ' + self.select_index + ':')
        print(self.df.iloc[int(self.select_index)][self.change])
        print('with new ' + self.change + ':')
        print(self.new_content)
        self.confirm = input('Confirm YES or NO: ')
        if self.confirm == 'YES':
            print('Updated existing ' + self.change + 'with:')
            print(self.new_content)

    def getQuestions(self):

        # DB module get all questions
        print('VIEW ALL QUESTIONS:')
        self.df = pd.read_csv('./res/trivial_purfruit_questions.csv')
        print(self.df.to_string())

if __name__ == "__main__":

    Database()

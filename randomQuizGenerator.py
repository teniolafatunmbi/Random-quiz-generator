#A quiz generator application in python.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery',
            'Alaska': 'Juneau', 
            'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 
            'California': 'Sacramento', 
            'Colorado': 'Denver',
            'Connecticut': 'Hartford', 
            'Delaware': 'Dover', 
            'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 
            'Hawaii': 'Honolulu', 
            'Idaho': 'Boise', 
            'Illinois':'Springfield', 
            'Indiana': 'Indianapolis', 
            'Iowa': 'Des Moines', 
            'Kansas':'Topeka', 
            'Kentucky': 'Frankfort', 
            'Louisiana': 'Baton Rouge', 
            'Maine':'Augusta', 
            'Maryland': 'Annapolis', 
            'Massachusetts': 'Boston', 
            'Michigan':'Lansing', 
            'Minnesota': 'Saint Paul', 
            'Mississippi': 'Jackson', 
            'Missouri':'Jefferson City', 
            'Montana': 'Helena', 
            'Nebraska': 'Lincoln', 
            'Nevada':'Carson City', 
            'New Hampshire': 'Concord', 
            'New Jersey': 'Trenton', 
            'New Mexico': 'Santa Fe', 
            'New York': 'Albany', 
            'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 
            'Ohio': 'Columbus', 
            'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 
            'Pennsylvania': 'Harrisburg', 
            'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 
            'South Dakota': 'Pierre', 
            'Tennessee': 'Nashville', 
            'Texas': 'Austin', 
            'Utah': 'Salt Lake City', 
            'Vermont': 'Montpelier', 
            'Virginia': 'Richmond', 
            'Washington': 'Olympia', 
            'West Virginia': 'Charleston', 
            'Wisconsin': 'Madison', 
            'Wyoming': 'Cheyenne'}
states = list(capitals.keys())

class quizGenerator(object):
    def __init__(self, states, capitals):
        self.states = states 
        self.capitals = capitals

    def createFile(self, quizFile, answerFile):
        quizFile.write("NAME:\nDATE:\nPERIOD:\n\n")
        quizFile.write(" " * 20 + "STATE CAPITAL QUIZ {}".format(quizNum + 1))
        quizFile.write("\n\n")

    def createQuestions(self, quizFile, wrong_answers, correct_answer):
        quizFile.write("{}. What is the capital of {}?".format(questionNum + 1, self.states[questionNum]))
        quizFile.write("\n\n")
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(list(capitals.values()), 3)
        answer_options = [correct_answer] + wrong_answers
        random.shuffle(answer_options)
        for i in range(4):
            quizFile.write("{}. {}".format("ABCD"[i], answer_options[i]))
            quizFile.write('\n')
        


    def createAnswers(self, answerFile, correct_answer):
        answerFile.write("{}. {} ".format(questionNum + 1, correct_answer))
        answerFile.write("\n\n")


Quiz = quizGenerator(states, capitals)

for quizNum in range(35):
    quizFile = open("capitalsquiz{}.txt".format(quizNum + 1), 'w')
    answerFile = open("answerfile{}.txt".format(quizNum + 1), 'w')
    Quiz.createFile(quizFile, answerFile)

    for questionNum in range(50):
        random.shuffle(states)
        correct_answer = capitals[states[questionNum]]
        wrong_answers = list(capitals.values())
        Quiz.createQuestions(quizFile, wrong_answers, correct_answer)
        quizFile.write("\n\n")
        Quiz.createAnswers(answerFile, correct_answer)
    quizFile.close()
    answerFile.close()

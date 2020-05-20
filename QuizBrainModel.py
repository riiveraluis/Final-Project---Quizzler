# QuizBrainModel.py
# Created by Luis Rivera Rivera on 3/31/20.
# Copyright © 2020 Luis Rivera Rivera. All rights reserved.

from Question import *


class QuizBrain:
    ''' Stores quizz data and send to the controller question text, score, answer and progress. '''
    def __init__(self):
        self.quiz = []
        self.loadQuestions()
        self.questionNumber = 0
        self.playerScore = 0

    def loadQuestions(self):
        questionFile = open("question.txt", "r")
        answerFile = open("answer.txt", "r")

        for question, answer in zip(questionFile, answerFile):
            self.quiz.append(Question(question, answer))

    def checkAnswer(self, userAnswer):
    
        if userAnswer + '\n' == self.quiz[self.questionNumber].answer:
            self.playerScore = self.playerScore + 1
            return True
        else:
            return False

    def getQuestionText(self):
        return self.quiz[self.questionNumber].question

    def getQuestionNumber(self):
        return self.questionNumber + 1

    def getTotalQuestions(self):
        return len(self.quiz)

    def nextQuestion(self):
        if self.questionNumber + 1 < len(self.quiz):
            self.questionNumber = self.questionNumber + 1
        else:
            self.playerScore = 0
            self.questionNumber = 0

    def getScore(self):
        return self.playerScore

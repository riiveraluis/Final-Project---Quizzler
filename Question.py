# Question.py
# Created by Luis Rivera Rivera on 3/31/20.
# Copyright © 2020 Luis Rivera Rivera. All rights reserved.


class Question:
    '''Work as an structure equivalent of a C++ or Swift written program. The purpose of class question is to store the question and
    the answer.'''

    def __init__(self, q, a):
        self.question = q
        self.answer = a

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

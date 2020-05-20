# EditQuestions.py
# Created by Gabriel Sierra Bello
# Copyright © 2020 Gabriel Sierra Bello. All rights reserved.

import Question


class FileProcessing:
    """ Responsible of solely saving new questions to file. """

    def __init__(self, Question):
        self.questionObj = Question
        self.WriteToFiles()

    def WriteToFiles(self):
        questionFile = open("question.txt", "a")
        answerFile = open("answer.txt", "a")

        if not self.questionAlreadyOnFile():
            questionFile.write(self.questionObj.getQuestion() + "\n")
            answerFile.write(self.questionObj.getAnswer()+"\n")

        questionFile.close()
        answerFile.close()

    def questionAlreadyOnFile(self):
        ''' Verifies is question to be added is already on file or not. '''
        flag = False
        questionFile = open("question.txt", "r")
        for i in questionFile:
            if i == self.questionObj.getQuestion() + '\n':
                flag = True

        return flag

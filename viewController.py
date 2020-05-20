# viewController.py
# Created by Luis Rivera Rivera on 3/31/20.
# Copyright © 2020 Luis Rivera Rivera. All rights reserved.

from quizView import QuizView
from QuizBrainModel import QuizBrain
from threading import Timer


class QuizApp():
    def __init__(self):
        self.quizBrain = QuizBrain()
        self.view, self.scoreLabel, self.progressLabel, self.questionLabel, self.trueButton, self.falseButton = QuizView().referenceView()
        self.updateUI()
        self.view.mainloop()

    def updateUI(self):
        self.questionLabel.configure(text=self.quizBrain.getQuestionText())
        self.scoreLabel.configure(
            text=str("Score: " + str(self.quizBrain.getScore())))
        self.progressLabel.configure(text=str(
            "Question " + str(self.quizBrain.getQuestionNumber()) + " of " + str(self.quizBrain.getTotalQuestions())))
        self.trueButton.configure(command=lambda: self.answerButtonPressed(self.trueButton), fg="black")
        self.falseButton.configure(command=lambda: self.answerButtonPressed(self.falseButton), fg="black")

    def answerButtonPressed(self, sender):
        userGotItRight = self.quizBrain.checkAnswer(sender.cget("text"))
        if userGotItRight:
            sender.configure(fg="green")
        else:
            sender.configure(fg="red")

        self.quizBrain.nextQuestion()

        timer = Timer(0.2, self.updateUI)
        timer.start()

# mainView.py
# Created by Luis Rivera Rivera on 3/31/20.
# Copyright © 2020 Luis Rivera Rivera. All rights reserved.

from tkinter import Tk, Label, Button, CENTER


class QuizView:
    ''' This view is the setup of the quiz screen '''
    def __init__(self):
        # Window setup
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.configure(bg="#313B5C")
        self.root.geometry("1000x600")

        # Widget setup
        self.scoreLabel = Label(
            self.root, text="Score: 0", bg="#313B5C", fg="white", font=("Helvetica", 21))

        self.progressLabel = Label(
            self.root, text="Question x of x.", bg="#313B5C", fg="white", font=("Helvetica", 21))

        self.questionLabel = Label(
            self.root, text="Question Text", bg="#313B5C", fg="white", font=("Helvetica", 21), wraplength=510, justify=CENTER, anchor=CENTER, height=7, width=44)

        self.trueButton = Button(self.root, height=2, width=18, text="True", font=(
            "Helvetica", 21), bg="#313B5C", fg="black")
        self.falseButton = Button(self.root, height=2, width=18, text="False", font=(
            "Helvetica", 21), bg="#313B5C", fg="black")

        # Object Drawing
        self.scoreLabel.place(x=30, y=25)
        self.progressLabel.place(x=420, y=25)
        self.questionLabel.place(x=245, y=140)
        self.trueButton.place(x=382, y=389)
        self.falseButton.place(x=382, y=500)

        self.root.resizable(0, 0)

    def referenceView(self):
        return self.root, self.scoreLabel, self.progressLabel, self.questionLabel, self.trueButton, self.falseButton

# mainMenu.py
# Created by Luis Rivera Rivera on 3/31/20.
# Copyright © 2020 Luis Rivera Rivera. All rights reserved.

from tkinter import Tk, Label, Button


class MainMenu:
    """ This view is the landing screen of the whole program it directs to quiz and adding question menu. """
    def __init__(self):
        self.mainMenuRoot = Tk()
        self.mainMenuRoot.title("Main Menu")
        self.mainMenuRoot.configure(bg="#313B5C")
        self.mainMenuRoot.geometry("400x280")

        self.titleLabel = Label(self.mainMenuRoot, text="Quizzler", font=(
            "Helvetica Neue", 32), bg="#313B5C", fg="white")
        self.startQuiz_Button = Button(
            self.mainMenuRoot, text="Start Game", bg="#313B5C",command=self.startQuiz)
        self.editQuestion_Button = Button(
            self.mainMenuRoot, text="Edit Quiz", width=8, bg="#313B5C",command=self.modifyQuestions)

        self.titleLabel.place(x=131, y=38)
        self.startQuiz_Button.place(x=155, y=115)
        self.editQuestion_Button.place(x=155, y=175)
        self.mainMenuRoot.resizable(0, 0)
        self.mainMenuRoot.mainloop()

    def startQuiz(self):
        import viewController
        self.mainMenuRoot.destroy()
        viewController.QuizApp()

    def modifyQuestions(self):
        import addQuestionView
        self.mainMenuRoot.destroy()
        addQuestionView.addQuestionToFile()


MainMenu()

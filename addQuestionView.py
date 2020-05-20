# addQuestionToFileView.py
# Created by Gamalier Rodriguez Delgado
# Copyright © 2020 Gamalier Rodriguez Delgado. All rights reserved.

from tkinter import Tk, Button, Label, Entry, Radiobutton, StringVar, SEL
from FileProcessing import *
from Question import *


class addQuestionToFile:
    def __init__(self):
        # Widget Creation
        self.root = Tk()
        self.root.title("Question Preferences")
        self.root.configure(bg="#313B5C")
        self.root.geometry("400x400")

        self.back_button = Button(self.root, text= "Back", command=self.goBackToMainMenu) 

        self.instructionLabel = Label(self.root, text="Enter New Question:", font=(
            "Helvetica Neue", 21), bg="#313B5C", fg="white")

        self.entryBox = Entry(self.root, width=25, bg="#FFFFFF")

        self.entryBox.insert(0, "Enter question")

        self.instructionLabel1 = Label(self.root, text="Select Answer:", font=(
            "Helvetica Neue", 21), bg="#313B5C", fg="white")

        self.selectionVar = StringVar()

        self.R1 = Radiobutton(self.root, text="True", font=(
            "Helvetica Neue", 18), fg="white", variable=self.selectionVar, value="True", command=SEL, bg="#313B5C")
        self.R2 = Radiobutton(self.root, text="False", font=(
            "Helvetica Neue", 18), fg="white", variable=self.selectionVar, value="False", command=SEL, bg="#313B5C")

        self.addQuestionToFileButton = Button(
            self.root, text="Add Question", bg="#313B5C", command=self.addQuestionToFile)

        # Widget Drawing
        self.back_button.place(x=8,y=7)
        self.instructionLabel.place(x=97, y=38)
        self.entryBox.place(x=75, y=107)
        self.instructionLabel1.place(x=123, y=172)
        self.R1.place(x=144, y=230)
        self.R2.place(x=144, y=273)
        self.addQuestionToFileButton.place(x=149, y=337)
        self.root.resizable(0, 0)
        self.root.mainloop()

    def goBackToMainMenu(self):
        import mainMenu
        mainMenu.MainMenu()
        self.root.destroy()


    def addQuestionToFile(self):
        FileProcessing(Question(self.entryBox.get(), self.selectionVar.get()))

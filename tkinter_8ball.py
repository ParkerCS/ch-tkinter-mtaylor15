# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding, image, borders, justification, whatever you can find in tkinter library etc.)  Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me out in checking your assignment)
from tkinter import *
from tkinter import font
from math import *
import random


class App():
    def __init__(self, master):
        # fonts
        self.title_font = font.Font(family="Times", size=25, weight=font.BOLD)
        self.instruct_font = font.Font(family="Times", size= 15)

        # Answer options
        self.answer_options = ["Yes","No","Maybe","Ask Again Later", "Probably", "Probably Not", "Most Likely", "I Have No Idea", "If I had To Guess, I Would Say No","Absolutely Not","Of Course","LOL No","No Way", "Does 1+1=2?"]

        # Variables
        self.input = StringVar()
        self.input.set("")
        self.answer = StringVar()

        self.my_string = StringVar()
        self.my_string.set("")

        # title
        self.title = Label(master, text="Magic 8 Ball", font= self.title_font)
        self.title.grid(column=1, row=1, columnspan=3, sticky='e' 'w')

        # Instructions
        self.instruct = Label(master, text= "Ask the Magic 8 Ball Any Yes or No Answer.  Proceed to click the 'Ask' button", font= self.instruct_font)
        self.instruct.grid(column=1, row=2, columnspan=3, sticky='e' 'w')

        # Input
        self.input_label = Label(master, text= "Enter your question here", font= self.instruct_font)
        self.input_label.grid(column=1, row=3)

        self.input_enter = Entry(master, textvariable= self.input)
        self.input_enter.grid(column=2, row=3)

        # Ask button
        self.ask_button = Button(master, text="ASK!", command= self.click)
        self.ask_button.grid(column=3, row=3)

        # Answer
        self.answer_label = Label(master, textvariable= self.my_string)
        self.answer_label.grid(column= 1, row= 4)

    def click(self):
        self.my_string.set(self.answer_options[random.randrange(len(self.answer_options))])



if __name__ == "__main__":
    root = Tk()
    root.title("8 Ball")
    app = App(root)
    root.mainloop()
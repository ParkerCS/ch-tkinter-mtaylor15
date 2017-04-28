# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.
from tkinter import *
from tkinter import font
from math import *


class App():
    def __init__(self,master):


        # Variables
        self.answer = DoubleVar()
        self.answer.set("")
        self.mass_1 = DoubleVar()
        self.mass_1.set("")
        self.mass_2 = DoubleVar()
        self.mass_2.set("")
        self.dist = DoubleVar()
        self.dist.set("")

        # Title
        self.title = Label(master, text="Marc's Gravity Calculator")
        self.title.grid(row=1, column=1, columnspan=4, sticky='e' + 'w')

        # Masses Label
        self.mass_1_label = Label(master, text="Mass One")
        self.mass_1_label.grid(row=2, column=1)

        self.mass_2_label = Label(master, text="Mass Two")
        self.mass_2_label.grid(row=3, column=1)

        # Mass Enter
        self.entry_mass1 = Entry(master, textvariable=self.mass_1)
        self.entry_mass1.grid(row=2, column=2)

        self.entry_mass2 = Entry(master, textvariable=self.mass_2)
        self.entry_mass2.grid(row=3, column=2)

        # Distance
        self.dist_label = Label(master, text="Distance Between Masses")
        self.dist_label.grid(row=4, column=1)
        self.dist_entry = Entry(master, textvariable=self.dist)
        self.dist_entry.grid(row=4, column=2)

        # Calculate Button
        self.calc = Button(master, text= "calculate", command=lambda: self.solve())
        self.calc.grid(row= 5, column=1)

        # Answer
        self.answer_label = Label(master, textvariable= self.answer)
        self.answer_label.grid(row=5, column=2)



    def solve(self):
        self.answer.set(self.mass_1.get() * self.mass_2.get() / self.dist.get() ** 2)


if __name__ == "__main__":
    root = Tk()
    root.title("Gravity Calc")
    app = App(root)
    root.mainloop()




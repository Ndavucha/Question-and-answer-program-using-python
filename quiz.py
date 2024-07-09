#!/usr/bin/env python
# coding: utf-8

# Import the required modules.
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
     
        self.openning_window = tkinter.Tk()
        self.openning_window.title("Quiz")
        
        # loading and reading the data
        
        try:
            with open ("data.txt", "r") as file:
                 self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tkinter.messagebox.showerror("Error", "Invalide file")
            self.openning_window.destroy()
            return
        
         # confirming the
        if len(self.data) < 5:
            tkinter.messagebox.showerror("Error", "Insufficient number of questions")
            self.openning_window.destroy()
            return

        # Initialize attributes
        self.current_question = 0
        self.score = 0

        # padding the widgets (framing)
        self.frame = tkinter.Frame(self.openning_window)
        self.frame.pack(padx=40, pady=40)

        self.question_label = tkinter.Label(self.frame, text="")
        self.question_label.pack(padx=10, pady=10)

        self.entry = tkinter.Entry(self.frame)
        self.entry.pack(padx=10, pady=10)

        self.submit_button = tkinter.Button(self.frame, text="Submit", command=self.check_answer)
        self.submit_button.pack(padx=10, pady=10)

        # the first question to be displayed
        self.show_question()

        # Main loop to start
        tkinter.mainloop()

        
        
    def show_question(self):
        # This method is responsible for displaying the current question and some other messages in the GUI.
        
        self.question_label.config(text=self.data[self.current_question]["your_question"])


    def check_answer(self):   
        # This method is responsible for checking if the user's answer is correct when the button is clicked.
        
        provided_answer = self.entry.get()
        final_answer = self.data[self.current_question]["answer"]

        if provided_answer.lower() == final_answer.lower():
            self.score += 1

        # Move to the next question or end the quiz
        self.current_question += 1

        if self.current_question < len(self.data):
            self.show_question()
        else:
            tkinter.messagebox.showinfo("Quiz Completed", f"Your score is {self.score}/{len(self.data)}")
            self.oppening_window.destroy()




# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()

# Reach me for more services(in research, projects, data, software development). charliendavu@gmail.com


# In[ ]:





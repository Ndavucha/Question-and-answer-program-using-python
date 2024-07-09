# Question-and-answer-program-using-python

### “admin.py” is a program with a Command-Line Interface (CLI).
####This program allows the user to manage a collection of quiz questions that are to be stored in a text file named “data.txt”.  JSON is usedto write and to read the data from the file back into Python.
####The program should then print a welcome message and enter an endless loop which starts by printing a list of options: “Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.” and then prompts the user to enter their choice. Once a choice has been entered, use an “if/elif” statement to handle each of the different choices.
####If the user enters “a” (add), prompt them to enter a question, then prompt them to enter as many answers as desired, and finally prompt them to enter the difficulty of the question, which must be an integer between 1 and 5. Place the details into a new dictionary with the structure shown on the previous page, and append the dictionary to the data list. Finally, write the entire data list to the text file in JSON format to save the data.
####If the user enters “l” (list), print a list of all the questions (just the question text, not the answers or difficulty) in the data list, preceded by their index number plus 1 (i.e. the first question listed should be number 1 instead of 0).
####If the user enters “s” (search), prompt them for a search term and then list the questions that contain the search term. Include the question’s index number plus 1 next to each result.
####If the user enters “v” (view), prompt them for an index number and then print details of the corresponding question in full. This should include the question text, answers, and difficulty.
####If the user enters “d” (delete), prompt them for an index number and then delete the corresponding question’s dictionary from the data list, then print a “Question deleted” message.
####If the user enters “q” (quit), print “Goodbye!” and break out of the loop to end the program.
####If the user enters anything else, print an “Invalid choice” message (the user will then be re-prompted for a choice on the next iteration of the loop).

### “quiz.py” is a program with a Graphical User Interface (GUI).
####This program uses the data from the “data.txt” file. Similar to the admin program, this program should load the data from the file once only - when the program begins. The program implements a simple quiz by displaying a series of randomly selected questions for the user to answer one at a time.
####Once the user types their answer and presses the Submit Answer button, the program checks whether what they typed matches one of the answers in the list of correct answers for the question and displays an appropriate messagebox.
####A different question is then displayed. After five questions have been answered, the program shows a final score and ends.

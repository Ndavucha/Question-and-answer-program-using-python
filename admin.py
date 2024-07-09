#!/usr/bin/env python
# coding: utf-8

# Import the json module to allow us to read and write data in JSON format.
import json
import os #ensuring the file is on the correct directory

# This function repeatedly prompts for input until an integer is entered.
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >=1:
                return value
            else:
                print ("enter an integer between 1 and 5")
        except ValueError:
            print ("enter an integer")
                      

# This function repeatedly prompts for input until something other than whitespace is entered.

def input_something(prompt):
    while True:
        enter_something = input(prompt).strip()
        if enter_something:
             return enter_something
        else:
             print ("please enter something!")

# Function to save data to "data.txt" in JSON format
def save_data(data_list):
    try:
        with open("data.txt", "w") as file:
            json.dump(data_list, file, indent=4) # arranging the json data to align properly
        print("Data saved.")
    except Exception as e:
        print("An error occurred while saving data:", e)

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
try:
    with open ("data.txt", "r") as file:
         data = json.load(file)
except FileNotFoundError:
    data = []
except json.JSONDecodeError:
    data = []

# Print welcome message, then enter the endless loop which prompts the user for a choice.
print('Welcome to the Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ')
        
    if choice == 'a':
        # Add a new question.
        
        your_question = input_something ("Enter the question")
        correct_answers = []
        while True:
            the_answer = input_something ("Enter a valid answer (enter 'q' when done)")
            if not the_answer:
                print("enter one answer")
            elif the_answer.lower() == 'q':
                if not correct_answers:
                    print("enter one answer")
                else:
                    break
            correct_answers.append(the_answer)  
        level_of_difficulty = input_int ("Enter question difficulty (1-5)")
        data.append ({"your_question": your_question, "correct_answers": correct_answers, "level_of_difficulty": level_of_difficulty})
        save_data(data)      
    
    elif choice == 'l':
        # List the current questions.
        
        if not data:
                    print("There are no questions saved.")
        else:
            
            [print(f"{i}: {item['your_question']}") for i, item in enumerate(data, start =1)]
                
    elif choice == 's':
        # Search the current questions.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("There are no questions saved.")
        else:
             please_enter_a_search_term = input_something("Enter a search term").lower()
             if_found = False
             for i, item in enumerate(data, start =1):
                 if please_enter_a_search_term in item['your_question'].lower():
                    print(f" {i}: {item['your_question']}")
                    if_found = True
             if not if_found:
                 print("The question cannot be found")       
                           
    elif choice == 'v':
        # View a question.
        
        if not data:
            print("There are no questions saved.")
        else:

            index_numbers = input_int("Enter the required index number")              
            if 1 <= index_numbers <= len (data):
                item = data [index_numbers - 1]
                print(f"your_question : {item['your_question']}")
                print("correct_answer:" if len (item['correct_answers']) > 1 else "correct_answer:")
                for correct_answer in item ['correct_answers']:
                    print (correct_answer)
                print(f"level_of_difficulty: {item['level_of_difficulty']}")
            else:
                print ("invalid index number")                             


    elif choice == 'd':
        # Delete a question.
        
        if not data:
            print("There are no questions saved.")
        else:
            index_numbers = input_int("Enter the required index number")              
            if 1 <= index_numbers <= len (data):                          
                del data [index_numbers -1]
                save_data(data)
                print("question deleted")
            else:
                print("invalid index number")
                                                                               
                                       
    elif choice == 'q':                                   
        # Quit the program.
        
        
        print("Goodbye!")

    else:
        # Print "invalid choice" message.
        
        print("invalid choice")


# reach out incase of anything or more intresting work-charliendavu@gmail.com





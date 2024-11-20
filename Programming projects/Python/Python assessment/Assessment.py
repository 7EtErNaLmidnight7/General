from config import *

score = 0
questions = 0
running = True

def question(q, a):
    global score, questions # idk why you need this

    print(str(questions+1) + ".")
    user_a = input(q + " ") # Prints question with input, space after question for readability

    if user_a.lower() == a.lower(): # Capital letters don't matter
        print(CORRECT_MSG)
        score = score + 1
        
    else:
        print(INCORRECT_MSG)
    questions += 1
    print(f"{score}/{questions}") # Stupid school making me do work
## START SETUP ##

print(OPENING)
name = input("Enter your name: ")
### QUESTIONS BEGIN HERE ###

def all_q(): # Enter questions here  
    question("What is the capital of Burundi?", "Gitega"),
    question("What is 6487246 mod 2348?", "2070"),
    question("What is your name again? ", name),
    question("What is the 4th letter of the alphabet?", " "),
    question("Is Sam Baillie the superior Sam?", "Yes"),
    question("What is the best programming language?", "c"),
    question("What are the whole contents of line 5 of the config file? (Not including stuff after the actual characters)", ""),              
    question("The answer is yes, please type it in", "yes"),
    question("This questions is sad, say hi to cheer him up", "hi"),
    question("What is 77 + 33?", "110"),
    question("Name an element healthier than the average lunchly", "uranium"),
    question("Am I better than 0liver Robinson at Celeste?", "Yes"),
    question("Can a match box?", "no"),
    question("What is the perfect christmas gift?", "A plutonium fuel rod"),
    question("What is the name of the spinning cat?", "Maxwell"),
    question("What is this https://www.youtube.com/watch?v=dQw4w9WgXcQ ?", "rickroll")
    question("What question number has an error?", "11")
    question("Why did the chicken cross the road?", "I don't bloody know")
    question("Did Hefest get that run?", "yes")
    question("What vscode theme am I using right now?", "Everforest dark")
    question("Did that tree just speak Viatnemese?", "idk")
    question("Type the letter a 50 times", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    question("Is this a simulation?", "yes")
    question("Lol this is not a simulation (press enter to continue)", "")
    question("Lol this is not a simulation (press enter to continue)", "")
    question("Lol this is not a simulation (press enter to continue)", "a")
    question("So that's where the missing a went (enter to continue)", "enter")
    question("Do you want to have anymore questions?", "no")
    question("TOO BAD (Enter a number to continue)", "a number")
    print("Nevermind, here you go")


while running:
    all_q()
    PRINT_SCORES(questions, score)

    idk_what_to_call_this_variable = input("Would you like to retry? (y, n) ")

    if idk_what_to_call_this_variable == "y":
        questions = 0
        score = 0

    else:
        print(GOODBYE)
        running = False
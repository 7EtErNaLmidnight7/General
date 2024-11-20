# Feel free to change some of the messages!

CORRECT_MSG = "Well done!\n"
INCORRECT_MSG = "Incorrect\n"

OPENING = """
    ||| Welcome to the quiz!                                                               |||
    ||| You may experience quite a lot of PAIN during this quiz, so buckle up and have fun |||
"""

SCORES = []

GOODBYE = "Hope you have a good rest of your day"

def PRINT_SCORES(questions, score):
    print(f"""
    You got {score}/{questions}!
    """
    )

    if score == questions:
        print("Well done for getting them all right!")

    elif score == 0:
        print("You suck quite a lot")

    elif score / questions == 0.5:
        print("Half correct, congratulations")

    elif score / questions < 0.5:
        print("You could've done better, but decent score")

    elif score / questions > 0.5:
        print("Nicely done!")

    else:
        print("Something went wrong!")

    good_var_name = input("Save score? (y, n) ")
    if good_var_name == "y":
        SCORES.append(score)

        for user_score in SCORES:
            print(user_score)
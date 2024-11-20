from random import choice

print("Welcome to the quiz of PAIN what is your name: ")
name = input().lower()

print(f"Hello {name}, get ready for PAAAIIIN")

running = True
questions = {
    "What is the capital city of Burrundi?": "gitega",
    "What is your name?": name,
    "Why did the chicken cross the road?": "idk",
    "What is the name of the question dictionary in this code?": "questions",
    "What is the best programming language?": "c",
    "What is the 4th letter in the alphabet?": " ",
    "Is Sam Baillie the superior Sam?": "yes",
    "What is 7/2?": "a number",
    "What is 34782484792 mod 3467223?": "2770879",
    "What is your permanent address?": "earth"
}

while running:
    if not(questions):
        print("Well done, now touch some grass")
        break
            
    question_list = list(questions.keys())    
    question = choice(question_list)

    print(question)
    answer = input().lower()

    if answer == questions[question]:
        print("You did a question, YIPEE")
        questions.pop(question)

    else:
        print("Get good lol")
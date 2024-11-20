global TASKS # I know global = bad, I just wanted it to look cleaner :)
TASKS = []

def add(): # Adds a task to the task list
    due_date = str(input("Enter date: "))
    task = str(input("Enter task: ")) # You don't have to remember capital placement :)))))

    TASK = [due_date, task]
    TASKS.append(TASK)


def remove():
    try:
        TASK_index = int(input("Enter task index: "))
        TASKS.pop(TASK_index)

# I spent ages on this function, only to realise I needed 2 lines lol (apart from making input work)
    except:
        print("Invalid index")


def help():
    print("""
          type "add" to add a task to the task list
          type "remove" to remove a completed task

          If you want to remove a task, you have to enter the task, I could implement a number feature,
          but am not bothered at the moment :D

          Task index is the what number the task is, starting at 0
          """) # Print statement looks wierd, don't know what it is though
         

def format():

    print("\n") # More readability, you're welcome :)
    for i in range(len(TASKS)):
        print(f"{i}:") # This is messy, bet there is another way to do this

        for segment in TASKS[i]:
            print(segment)
        print("\n")
            

print(""" type "help" for help """) # Runs once to avoid annoyance

while True: # Loop for app
    format() # Opens task table when an action is completed
    cmd = input().lower() # "cmd" is command

    if cmd == "add":
        add()
    
    elif cmd == "remove":
        remove()
    
    elif cmd == "help":
        help()

    else:
        print("Unknown command")
    
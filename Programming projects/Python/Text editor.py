def new(files):
    counter = 0
    file = []

    while True:
        counter += 1
        line = input(f"{counter}. ")
        
        if line == "save": # Enter "save" to save your file
            break
        file.append(line)

    name = input("Enter file name: ")
    files[name] = file

def search(files):
    for file in files.keys():
        print(file)

    file_to_search = input("Enter file you would like to view: ")
    file_to_print = files.get(file_to_search, "No such file exists")
    print("\n".join(file_to_print))  

def delete(files):
    for file in files.keys():
        print(file)

    file_to_delete = input("Enter file to delete: ")
    check = input("Continue? (y for yes, n for no)")
    if check == "y":
        files.pop(file_to_delete, "Error")

files = {}
while True:
    cmd = input()
    if cmd == "new":
        new(files)
    elif cmd == "search":
        search(files)
    elif cmd == "delete":
        delete(files)
    else:
        print("No such function")
        

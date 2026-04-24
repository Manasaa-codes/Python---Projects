tasks = []
try:
    with open("tasks.txt","r") as file:
        tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
except FileNotFoundError:
    pass
def save_tasks(tasks):
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task+"\n")
while True:
    print ("\n1. Add Task")
    print ("2. View Tasks")
    print("3. Delete Task")
    print("4.Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if choice == 1:
        task = input("Enter the name of the task to be added : ")
        tasks.append(task)
        save_tasks(tasks)
    elif choice == 2:
        if(len(tasks) == 0):
            print("No Tasks Available")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    elif choice == 3:
        num = int(input("Enter the number to be deleted : "))
        if (1 <= num <= len(tasks)):
            tasks.pop(num-1) 
            save_tasks(tasks)
        else :
            print("Invalid Task Number")
    elif choice == 4:
        break
    else :
        print("Invalid Choice")
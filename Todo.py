todo_list = []


def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "Pending"})
    print("New Task Added Successfully!")


def view_task():
    print("Your Todo List: ")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task}")


def menu():
    while(True):
        print("*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View All Task")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice! Try again!!!")

menu()
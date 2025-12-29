import json
import os

FILE = "tasks.json"

def load_data():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_task(tasks):
    name = input("Task name: ")
    priority = input("Priority (High/Low): ")
    due_date = input("Due date (YYYY-MM-DD): ")
    category = input("Category: ")

    task = {
        "name": name,
        "priority": priority,
        "due_date": due_date,
        "category": category,
        "status": "Pending"
    }

    tasks.append(task)
    print("✅ Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']} | {task['priority']} | {task['due_date']} | {task['category']} | {task['status']}")

def mark_completed(tasks):
    view_tasks(tasks)
    index = int(input("Select task number: ")) - 1
    tasks[index]["status"] = "Completed"
    print("✅ Task marked as completed!")

def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Select task number: ")) - 1
    tasks.pop(index)
    print("🗑️ Task deleted!")

def main():
    data = load_data()
    username = input("Enter username: ")

    if username not in data:
        data[username] = []

    tasks = data[username]

    while True:
        print("\n1.Add  2.View  3.Complete  4.Delete  5.Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_data(data)
            print("💾 Saved. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
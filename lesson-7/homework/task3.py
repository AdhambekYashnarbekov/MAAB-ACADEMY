import json
import os

todoList = {}

class ToDoList:
    def __init__(self, taskID, title, description, dueDate, status):
        self.taskID = taskID
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.status = status

class TodoListManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.todoList = {}
        self.load_records()

    def load_records(self):
        try:
            with open(self.filename, "r") as f:
                self.todoList = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.todoList = {}

    def save_records(self):
        with open(self.filename, "w") as f:
            json.dump(self.todoList, f, indent=4)

    def add_task(self):
        taskID = int(input("Enter Task ID: "))
        title = input("Enter Task Title: ")
        description = input("Enter Task Description: ")
        dueDate = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")

        self.todoList[str(taskID)] = {
            "title": title,
            "description": description,
            "dueDate": dueDate,
            "status": status,
        }
        self.save_records()
        print("Task added successfully!")

    def view_all_tasks(self):
        if self.todoList:
            print("Tasks:")
            for taskID, details in self.todoList.items():
                print(
                    f"{taskID}, {details['title']}, {details['description']}, {details['dueDate']}, {details['status']}"
                )
        else:
            print("No tasks found.")

    def update_task(self):
        taskID = input("Enter Task ID to update: ")
        if taskID in self.todoList:
            print("If you don't want to change something, leave it blank!")
            title = input("Enter new Task title: ")
            description = input("Enter new description: ")
            dueDate = input("Enter new due date: ")
            status = input("Enter new status (Pending/In Progress/Completed): ")

            if title:
                self.todoList[taskID]["title"] = title
            if description:
                self.todoList[taskID]["description"] = description
            if dueDate:
                self.todoList[taskID]["dueDate"] = dueDate
            if status:
                self.todoList[taskID]["status"] = status
            self.save_records()
            print("Task updated successfully!")
        else:
            print("Task ID not found.")

    def delete_task(self):
        taskID = input("Enter the task ID: ")
        if taskID in self.todoList:
            del self.todoList[taskID]
            self.save_records()
            print("The Task successfully deleted!")
        else:
            print("No task found with this ID")

    def filter_tasks(self):
        status_filter = input("Enter status to filter (Pending/In Progress/Completed): ")
        filtered_tasks = {}
        for taskID, details in self.todoList.items():
            if details["status"].lower() == status_filter.lower():
                filtered_tasks[taskID] = details
        if filtered_tasks:
            print(f"Tasks with status '{status_filter}':")
            for taskID, details in filtered_tasks.items():
                print(
                    f"{taskID}, {details['title']}, {details['description']}, {details['dueDate']}, {details['status']}"
                )
        else:
            print(f"No tasks found with status '{status_filter}'.")

# Main Execution
todoListManager = TodoListManager()

while True:
    print("\nWelcome to the To-Do Application!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Filter tasks by status")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        todoListManager.add_task()
    elif choice == "2":
        todoListManager.view_all_tasks()
    elif choice == "3":
        todoListManager.update_task()
    elif choice == "4":
        todoListManager.delete_task()
    elif choice == "5":
        todoListManager.filter_tasks()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
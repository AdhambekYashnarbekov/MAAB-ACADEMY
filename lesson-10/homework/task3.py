import json
import csv

class TaskManager:
    def __init__(self, filename="tasks.json"):
        """Initialize TaskManager with a filename."""
        self.filename = filename
        self.tasks = []

    def load_tasks(self):
        """Load tasks from tasks.json into a list of dictionaries."""
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: JSON decoding failed.")

    def display_tasks(self):
        """Display all tasks with their details."""
        print("\nTasks List:")
        print(f"{'ID':<5} {'Task Name':<20} {'Completed':<10} {'Priority':<10}")
        print("=" * 50)
        for task in self.tasks:
            print(f"{task['id']:<5} {task['task']:<20} {task['completed']:<10} {task['priority']:<10}")

    def save_tasks(self):
        """Save tasks back to the JSON file."""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def calculate_statistics(self):
        """Calculate and display task completion statistics."""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task["completed"])
        pending_tasks = total_tasks - completed_tasks
        total_priority = sum(task["priority"] for task in self.tasks)
        average_priority = total_priority / total_tasks if total_tasks > 0 else 0

        stats = {
            "Total tasks": total_tasks,
            "Completed tasks": completed_tasks,
            "Pending tasks": pending_tasks,
            "Average priority": round(average_priority, 2),
        }

        print("\nTask Statistics:")
        for key, value in stats.items():
            print(f"{key}: {value}")

    def write_tasks_to_csv(self, output_filename="tasks.csv"):
        """Convert JSON tasks to CSV format."""
        with open(output_filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Task", "Completed", "Priority"])  # Header row
            for task in self.tasks:
                writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
        print(f"\nTasks successfully written to {output_filename}")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.load_tasks()
    task_manager.display_tasks()
    task_manager.calculate_statistics()
    task_manager.write_tasks_to_csv()

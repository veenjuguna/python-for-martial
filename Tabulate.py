from Tabulate import tabulate
from datetime import datetime
import os
import sys
import json
import time

# Welcome the user
def welcome_user():
    print("Welcome to Your Personal Task Manager!")
    print("Let’s streamline your productivity and achieve your goals.\n")

    # Task structure
tasks = []

# Add a sample task for demonstration
def initialize_tasks():
    tasks.append({"Title": "Complete Python Project", "Priority": "High", "Status": "Pending", "Deadline": "2025-01-30"})


    # Add a new task
def add_task(title, priority, status, deadline):
    tasks.append({"Title": title, "Priority": priority, "Status": status, "Deadline": deadline})
    print("Task added successfully!\n")

# View all tasks
def view_tasks():
    from tabulate import tabulate
    print(tabulate(tasks, headers="keys", tablefmt="grid"))

    # Update task status
def update_status(task_index, new_status):
    try:
        tasks[task_index]["Status"] = new_status
        print("Task status updated!\n")
    except IndexError:
        print("Invalid task index.\n")

        # Delete completed tasks
def delete_completed_tasks():
    global tasks
    tasks = [task for task in tasks if task["Status"] != "Completed"]
    print("Completed tasks deleted!\n")
# Main function
def main():
    welcome_user()
    initialize_tasks()

    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update task status")
        print("4. Delete completed tasks")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            title = input("Enter task title: ").strip()
            priority = input("Enter priority (High/Medium/Low): ").strip()
            status = input("Enter status (Pending/In Progress/Completed): ").strip()
            deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
            add_task(title, priority, status, deadline)
        elif choice == "3":
            task_index = int(input("Enter task index to update: ").strip())
            new_status = input("Enter new status: ").strip()
            update_status(task_index, new_status)
        elif choice == "4":
            delete_completed_tasks()
        elif choice == "5":
            print("Exiting Task Manager. Stay productive!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:30:43 2023

@author: srinidhi
"""

import datetime


tasks = {}


def create_task():
    task_description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    status = "Incomplete"
    task_id = len(tasks) + 1
    tasks[task_id] = {"description": task_description, "due_date": due_date, "status": status}
    print(f"Task {task_id} created.")


def update_task():
    task_id = int(input("Enter the task ID to update: "))
    if task_id in tasks:
        new_status = input("Enter the new status (Incomplete/Complete): ").capitalize()
        if new_status in ["Incomplete", "Complete"]:
            tasks[task_id]["status"] = new_status
            print(f"Task {task_id} status updated to {new_status}.")
        else:
            print("Invalid status. Please enter 'Incomplete' or 'Complete'.")
    else:
        print(f"Task {task_id} not found.")


def track_tasks():
    current_date = datetime.date.today()
    print("Tasks to do:")
    for task_id, task in tasks.items():
        due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        if task["status"] == "Incomplete" and due_date >= current_date:
            print(f"Task {task_id}: {task['description']} (Due on {task['due_date']})")


while True:
    print("\nOptions:")
    print("1. Create a new task")
    print("2. Update task status")
    print("3. Track tasks")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        create_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        track_tasks()
    elif choice == "4":
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")



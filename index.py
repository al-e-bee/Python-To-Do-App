# ====================
# 1. IMPORTS
# ====================
import math

# =========================
# 2. FUNCTION DEFINITIONS
# =========================

def greet_user(name):
    print(f"Welcome {name}!")

def show_user_menu(menu_list):
    print("---- MAIN MENU ----")
    for index, option in enumerate(menu_list, 1):
        print(f"{index}. {option}")
    choice = input("\nPlease enter the number of your choice: ").strip()
    return choice

def add_task(tasks):
    new_task = input("\nEnter the task you want to add:  ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"✅ Success: '{new_task}' added to your list.")
    else:
        print("❌ Error: Task cannot be blank!")
    
user_menu_list = ["Add task", "View tasks", "Delete tasks", "Quit application"]
user_tasks = []

greet_user("Ali")

while True:
    user_choice = show_user_menu(user_menu_list)
    
    if user_choice == "1":
        add_task(user_tasks)
        print(f"Current tasks: {user_tasks}\n")
    
    elif user_choice == "2":
        print("\n---YOUR TASKS ---")
        if not user_tasks:
            print("Your list is empty!")
        else:
            for i, task in enumerate(user_tasks, 1):
                print(f"{i}. {task}")
        print()
    
    elif user_choice == "3":
        print("\nDelete functionality coming up next!")
        
    elif user_choice == "4":
        print("\nthank you for using To-Do App! Goodbye.")
        break
    
    else:
        print("\n⚠️ Invalid selection. Please type 1, 2, 3, or 4.\n")

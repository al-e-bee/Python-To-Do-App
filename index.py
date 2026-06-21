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
# =========================
# 1. FUNCTION DEFINITIONS
# =========================

def greet_user(name):
    print(f"Welcome {name}!")

def show_user_menu(menu_list, should_print_details):
    if should_print_details:
        print("\n---- MAIN MENU ----")
        for index, option in enumerate(menu_list, 1):
                print(f"{index}. {option}")
        print("---------------")
        prompt = "Please enter your choice (1 - 4): "
    else:
        prompt = "Enter choice (or press Enter to view menu choices again): "
    choice = input(prompt).strip()

    if choice == "":
        return choice, True
    return choice, False
    
def add_task(tasks):
    new_task = input("\nEnter the task you want to add:  ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"✅ Success: '{new_task}' added to your list.")
    else:
        print("❌ Error: Task cannot be blank!")
        
def delete_task(tasks):
    if not tasks: 
        print("\n❌ Error: Your to-do list is empty. There is nothing to delete.")
        return
    print("\n--- DELETE A TASK ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    try:
        task_num = input("\nEnter the number of the task you want to delete: ").strip()
        index_to_delete = int(task_num) - 1
        
        removed_task = tasks.pop(index_to_delete)
        print(f"✅ Success: '{removed_task}' has been removed.")
    
    except ValueError:
        print("❌ Invalid Input: Please enter a valid whole number (e.g., 1, 2).")
    except IndexError:
        print("❌ Out of Bounds: That task number does not exist in your list.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    finally:
        print("Returning to main menu tracker...")
        
# =========================================
# 2. GLOBAL VARIABLES & APP INITIALIZATION
# =========================================    
user_menu_list = ["Add task", "View tasks", "Delete tasks", "Quit application"]
user_tasks = []

greet_user("Ali")
menu_requested = True

# ========================================
# 3. MAIN RUNTIME LOOP
# ========================================
while True:
   user_choice, menu_requested = show_user_menu(user_menu_list, menu_requested)
   
   if user_choice == "":
       continue
    
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
        delete_task(user_tasks)
        print()
        
   elif user_choice == "4":
        print("\nThank you for using To-Do App! Goodbye.")
        break
    
   else:
        print("\n⚠️ Invalid selection. Please choose an option from 1 to 4.\n")
        menu_requested = True

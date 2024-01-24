tasks = []

def Display_menu():
     print('\n*** Todo List ***')
     print('1. Add task')
     print('2. wiew all task')
     print('3. Mark tasks as comlete')
     print('4. set a priority for a task')
     print('5. set a due date for a task')
     print('6. EXIT')

def add_task():
     task_name = input('Enter task : ')
     tasks.append(task_name)
     print('Added task sussesfully')

def Display_task():
     if tasks:
          print('\n your task : ')
          for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
     else:
        print("\nNo tasks to display.")

def mark_complete():
    task_number = int(input("Enter the number of the task to mark as complete: "))
    tasks[task_number-1] = tasks[task_number-1] + " (Completed)"  # Modify the task
    print("Task marked as complete!")

def set_priority():
    task_number = int(input("Enter the number of the task to set priority: "))
    priority = input("Enter the priority (high, medium, low): ")
    tasks[task_number-1] = f"[{priority}] {tasks[task_number-1]}"  # Add priority to the task
    print("Priority set successfully!")

def set_due_date():
       pass

while True:
    Display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        Display_task()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        set_priority()
    elif choice == '5':
        set_due_date()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

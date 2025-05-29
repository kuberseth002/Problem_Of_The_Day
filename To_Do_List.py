tasks = []

def add_task(task: str):
    """
    Add a new task to the tasks list if it doesn't already exist.

    Args:
        task (str): The task to be added.
        
    Prints:
        Confirmation message whether the task was added or already exists.
    """
    if task not in tasks:
        tasks.append(task)
        print("Task added:", task)
    else:
        print("Task already exists:", task)

def remove_task(task: str):
    """
    Remove a task from the tasks list if it exists.

    Args:
        task (str): The task to be removed.

    Prints:
        Confirmation message whether the task was removed or not found.
    """
    if task in tasks:
        tasks.remove(task)
        print("Removed task:", task)
    else:
        print("Task not found:", task)

def main():
    """Main function to collect tasks, remove some, and display the remaining."""

    for i in range(1, 5):
        user_task = input(f"Enter task {i}: ")
        add_task(user_task)

    for _ in range(2):
        if tasks:
            remove_task(tasks[0])
        else:
            print("No tasks left to remove.")

    if tasks:
        print("\nCurrent Task List:")
        for task in sorted(tasks):
            print("-", task)
    else:
        print("\nError: No tasks in the list!")

if __name__ == "__main__":
    main()

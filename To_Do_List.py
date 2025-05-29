lst = []

lst1 = input("Enter task1: ")
lst2 = input("Enter task2: ")
lst3 = input("Enter task3: ")
lst4 = input("Enter task4: ")

def add_task(task):
    if task not in lst:
        lst.append(task)
        print("task added:", task)
    else:
        print("it already exists:", task)

add_task(lst1)
add_task(lst2)
add_task(lst3)
add_task(lst4)

if lst1 in lst:
    lst.remove(lst1)
    print("removed task:", lst1)
else:
    print("task not found:", lst1)

if lst2 in lst:
    lst.remove(lst2)
    print("removed task:", lst2)
else:
    print("task not found:", lst2)

if len(lst) > 0:
    print("\nCurrent Task List:")
    for task in sorted(lst):
        print("-", task)
else:
    print("\nError: No tasks in the list!")

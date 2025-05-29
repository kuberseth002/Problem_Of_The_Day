lst = []

lst1 = input("Enter task1:")
lst2 = input("Enter task2:")
lst3 = input("Enter task3:")
lst4 = input("Enter task4:")


#Adding
if lst1 not in lst:
    lst.append(lst1)
    print("task added:", lst1)
else:
    print("it already exist:", lst1)

if lst2 not in lst:
    lst.append(lst2)
    print("task added:", lst2)
else:
    print("it already exist:", lst2)

if lst2 not in lst:
    lst.append(lst2)
    print("task added:", lst2)
else:
    print("it already exists:", lst2)

# Removing
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
    print("\n Current Task List:")
    for lst in sorted(lst):
        print("-", lst)
else:
    print("\n Error: No tasks in the list!")


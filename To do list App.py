tasks = []
while True:
    print("\n=== To Do List ===")
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task:")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        print("\n Your Tasks:")
        for i in range(len(tasks)):
            print(i+1, "-", tasks[i])

    elif choice == "3":
            num = int(input("Enter task number number"))
            if num < len(tasks):
                tasks.pop(num -1)
                print("Task Removed!")
            else:
                print("Invaild Number")

    elif choice =="4":
        print("Good Bye👋")
        break
    else:
        print("invaild Number Plaese Try Again")
        break
    else:
        print("invaild Number Plaese Try Again")
    

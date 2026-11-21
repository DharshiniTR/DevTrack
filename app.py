def add_task():
    task = input("Enter your task: ")
    print(f"Task added: {task}")



def view_tasks():
    print("Your tasks will appear here.")


def main():
    print("\n===== DevTrack =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice!")
=======
def main():
    print("Welcome to DevTrack!")
    add_task()



if __name__ == "__main__":
    main()
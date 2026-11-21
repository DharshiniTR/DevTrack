def add_task():
    task = input("Enter your task: ")
    print(f"Task added: {task}")


def main():
    print("Welcome to DevTrack!")
    add_task()


if __name__ == "__main__":
    main()
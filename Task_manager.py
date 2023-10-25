def task_manager() -> None:

    manage_list = int(input("How many tasks do you have? "))

    tasks_list = [input(f"What is task number ({j+1})? ") for j in range(manage_list)]

    print(f"I listed these tasks for you: {tasks_list}")

if __name__ == "__main__":
    task_manager()
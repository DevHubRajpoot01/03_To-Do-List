''' Create a To-Do-List app '''

# A file for save the tasks:
data = "tasks.txt"

# Load data from a file
def load_data():
    try:
        with open(data,'r') as file:
            content = [line.strip() for line in file.readlines()]
            return content
    except FileNotFoundError:
        return []        
    except Exception as e:
        print(f"exception: {e}")

# Save updated data 
def save_data(tasks):
    with open(data,'w') as file:
        for task in tasks:
            file.write(task + "\n") 

# Let's Define a func for add tasks:
def add_task(task,tasks):
    tasks.append(task)
    save_data(tasks)
    print('Task added succesfully!')
    print("*"*40)

# Let's Define a func for show list of tasks:
def show_tasks(tasks):
    if tasks == []:
        print("Your To-Do-List is empty!")
    else:
        print("Your To-Do-List is here:")    
        for i, j in enumerate(tasks,start=1):
            print(f"{i}. {j}")
        print("*"*40)

# Let's Define a func for remove task:
def remove_task(task_no,tasks):   
    if 1 <= task_no <= len(tasks):
        for i, task in enumerate(tasks, start=1):
            if i == task_no:
                tasks.pop(i-1)
                save_data(tasks)
                print(f"task no. {i} has removed.")
    else:
        print("Invalid task number; Please try again!")
    print("*"*40)          

# Program starts from here:
def main():
    tasks = load_data()
    print("Welcome in To-Do-List")
    print("*"*40)
    print("press 1 for add task")
    print("press 2 for show tasks")
    print("press 3 for remve task")
    print("press 4 for exit")
    while True:
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                task = input("Write your task here: ")
                add_task(task,tasks)
            case "2":
                show_tasks(tasks)
            case "3":
                task_no = int(input("Enter task no which you wanna delete: "))
                remove_task(task_no,tasks)
            case "4": 
                print("Bye Bye! \nSee You!")
                break
            case _:
                print("invalid choice; please choose again!")

if __name__ == "__main__":
    main()
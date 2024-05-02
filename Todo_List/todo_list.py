# This is a simple todo-list program
# It asks the user for tasks to be added to the list
# Then, it asks them again for completed tasks to be removed from the list or the day ends before they finish all the tasks

def main():
    todo_list = []
    adding_tasks(todo_list)
    print(todo_list)
    removing_completed_tasks(todo_list)

def adding_tasks(todo_list):
    while True:
        task = input('Add a task to your list(type "done" when finished): ').lower()
        while not task.isalpha():
            task = input('Please enter a valid task(type "done" when finished): ').lower()
        if task == 'done':
            break
        todo_list.append(task)

def removing_completed_tasks(todo_list):
    message = ""
    while len(todo_list) and message != 'byebye':
        message = input("Add a task you've done(type 'byebye' when finished): " ).lower()
        while not message.isalpha():
            message = input("Please add a valid task you've done(type 'byebye' when finished): " ).lower()
        if message in todo_list:
            todo_list.remove(message)
        print(todo_list)

main()

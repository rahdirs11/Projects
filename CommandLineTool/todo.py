import sys, os
from time import sleep
from datetime import datetime

pending, completed = 0, 0

def _rewriteTodoTasks(tasks: list):
    with open('todo.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def _listOfIncompleteTasks() -> list:
    with open('todo.txt', 'r') as file:
        todoTasks = [
            task.rstrip()
            for task in file.readlines()
        ]
    return todoTasks


def _listOfCompletedTasks() -> list:
    with open('done.txt', 'r') as file:
        completedTasks = [
            task.rstrip()
            for task in file.readlines()
        ]
    return completedTasks

def help():
    print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')


def delete(number: int):
    global pending
    if os.path.exists('todo.txt'):
        if number <= 0 or number > pending:
            print(f'Error: todo #{number} does not exist. Nothing deleted.')
        else:
            if pending > 0:
                pending -= 1
                print(f'Deleted todo #{number}')
                # reading all incomplete tasks except the one that has to be deleted
                with open('todo.txt', 'r') as file:
                    todoTasks = [
                        task.rstrip()
                        for i, task in enumerate(file.readlines())
                        if i != number - 1
                        ]
                        # re-writing the todo.txt with the remaining tasks to be done
                    _rewriteTodoTasks(todoTasks)
            else:
                print('No more tasks left!!!') # work on this as well


def done(number: int):
    global completed, pending
    # print('This is to mark a task as finished!!')
    if number <= 0 or number > pending:
        print(f'Error: todo #{number} does not exist.')   # work on the alternative for this, the actual I mean
    else:
        completed += 1
        print(f'Marked todo #{number} as done.')
        # extracting the
        with open('todo.txt', 'r') as file:
            todoTasks, completedTask = list(), str()
            for i, task in enumerate(file.readlines()):
                if i + 1 == number:
                    completedTask = task
                else:
                    todoTasks.append(task.rstrip())
            # print(todoTasks)

        pending -= 1
        # re-writing the todo.txt file with the remaining tasks to be done
        _rewriteTodoTasks(todoTasks)

        # adding the completed task to the completed.txt file
        with open('done.txt', 'a') as file:
            file.write(f'x {datetime.strftime(datetime.now(), "%Y-%m-%d")} {completedTask}')



def ls():
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        if len(tasks) == 0:
            print('There are no pending todos!')
        else:
            # prints in reverse order
            for i in range(len(tasks) - 1, -1, -1):
                print(f'[{i + 1}] {tasks[i].rstrip()}')


def report():
    global pending, completed
    pending = len(_listOfIncompleteTasks())
    completed = len(_listOfCompletedTasks())
    print(f'{datetime.strftime(datetime.now(), "%Y-%m-%d")} Pending : {pending} Completed : {completed}')


def add(task: str=None):
    global pending
    pending += 1
    print(f'Added todo: "{task}"')
    with open('todo.txt', 'a') as file:
        file.write(task + '\n')


if __name__ == '__main__':
    file1Exists = os.path.exists('todo.txt')
    file2Exists = os.path.exists('done.txt')
    if file1Exists:
        todoTasks = _listOfIncompleteTasks()
        pending = len(todoTasks)
    else:
        with open('todo.txt', 'w') as file:
            pass
        pending = 0

    if not file2Exists:
        with open('done.txt', 'w') as file:
            pass
        completed = 0
    else:
        with open('done.txt', 'r') as file:
            completedTasks = [
                task.rstrip()
                for task in file.readlines()
            ]
            completed = len(completedTasks)
    args = sys.argv
    # print(args, len(args))
    # print(args[1])
    if len(args) == 1:
        help()
        print()
    elif len(args) == 2:
        if args[1] == 'report':
            report()
        elif args[1] == 'help':
            help()
            print()
        elif args[1] == 'ls':
            ls()
        elif args[1] == 'add':
            print("Error: Missing todo string. Nothing added!")
        elif args[1] == 'done':
            print('Error: Missing NUMBER for marking todo as done.')
        elif args[1] == 'del':
            print('Error: Missing NUMBER for deleting todo.')
    else:
        if args[1] == 'del':
            # if args[2]:
            delete(int(args[2]))
        elif args[1] == 'add':            
            # if args[2] and args[2][0] == '"' and args[2][0] == '"':
            add(args[2])
            # else:
            #     print("Error: Missing todo string. Nothing added!")
        elif args[1] == 'done':
            # print(type(args[2]))
            if args[2]:
                done(int(args[2]))
            else:
                print('Error: Missing NUMBER for marking todo as done.')
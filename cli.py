from time import strftime

from function import *
import time
now=strftime("%b %d,%y  %H:%M:%S")
print("it is",now)
while True:
    user_action=input("Type add,show,edit,complete or Exit:").lower()
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo=user_action[4:]
        todos=get_todos()
        todos.append(todo+"\n")
        write_todos(todos)
    elif user_action.startswith("show"):
        todos=get_todos()
        for index,item in enumerate(todos):
            row=f"{index + 1}-{item.strip()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            number=number-1
            todos=get_todos()
            new_todo=input("Enter new Todo:")
            todos[number]=new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Invalid input")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos=get_todos()
            index=number-1
            todo_to_remove=todos[index]
            todos.pop(number-1)
            write_todos(todos)
            print(f"todo {todo_to_remove} is remove from todos")
        except IndexError:
            print("There is no item of this range")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input")
print("Thank you for your time")



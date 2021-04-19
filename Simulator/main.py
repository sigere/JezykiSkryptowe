import os
from Queue import Queue
from Stack import Stack


def print_status(item):
    if type(item) == Queue:
        print(f'''
Queue Simulator
Queue: {item.print()}
''')
        if item.last_pop:
            print(f'Popped: {item.last_pop}')
            item.last_pop = None
        print_help()
    elif type(item) == Stack:
        print(f'''  
Stack Simulator
Stack: {item.print()}
''')
        if item.last_pop:
            print(f'Popped: {item.last_pop}')
            item.last_pop = None
        print_help(item)


def print_help(item):
    struct = "queue" if type(item) == Queue else "stack"
    print(f'''
a, append       -   append value to the {struct}
p, pop          -   pop last element from the {struct}
s, sort         -   sort queue the {struct}
q, quit, exit   -   terminate program
    ''')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


dictionary = {
    "a": 1,
    "append": 1,
    "p": 2,
    "pop": 2,
    "s": 3,
    "sort": 3,
    "q": 0,
    "quit": 0,
    "exit": 0
}
cls()
a = str(input("Choose queue or stack> "))
if a == 'queue':
    print("The Queue Simulator")
    ok = False
    capacity = 0
    while not ok:
        try:
            capacity = int(input("Set capacity of the queue> "))
            if capacity <= 0:
                raise ValueError
            ok = True
        except ValueError:
            print("Invalid value!")

    q = Queue(capacity)
    while True:
        cls()
        print_status(q)
        choice = dictionary.get(input("> ").lower(), -1)
        if choice == 1:
            value = input("value> ")
            if not q.append(value):
                print("Queue is full")
        elif choice == 2:
            value = q.pop()
            if not value:
                print("Queue is empty")
        elif choice == 3:
            q.sort()
        elif choice == 0:
            break
        else:
            print("Invalid command")
            print_help()
        q.print()
        if q.is_empty():
            print("The queue is empty")
        else:
            print("The queue is not empty")
if a == 'stack':
    print("The Stack Simulator")
    ok = False
    capacity = 0
    while not ok:
        try:
            capacity = int(input("Set capacity of the stack> "))
            if capacity <= 0:
                raise ValueError
            ok = True
        except ValueError:
            print("Invalid value!")

    s = Stack(capacity)
    while True:
        cls()
        print_status(s)
        choice = dictionary.get(input("> ").lower(), -1)
        if choice == 1:
            value = input("value> ")
            if not s.append(value):
                print("Stack is full")
        elif choice == 2:
            value = s.pop()
            if not value:
                print("Stack is empty")
        elif choice == 3:
            s.sort()
        elif choice == 0:
            break
        else:
            print("Invalid command")
            print_help()
        s.print()
        if s.is_empty():
            print("The stack is empty")
        else:
            print("The stack is not empty")
print("bye")

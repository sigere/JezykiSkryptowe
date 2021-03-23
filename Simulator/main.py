import os
from Queue import Queue


def print_status(queue):
    print(f'''
Queue Simulator

Queue: {queue.print()}
''')
    if queue.last_pop:
        print(f'Popped: {queue.last_pop}')
        queue.last_pop = None
    print_help()


def print_help():
    print('''
a, append       -   append value to the queue
p, pop          -   pop first element from the queue
s, sort         -   sort queue the queue
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
print("bye")

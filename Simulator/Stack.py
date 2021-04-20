class Stack:

    def __init__(self, size):
        self.s = [None] * size  # list to store stack elements
        self.capacity = size  # maximum capacity of the stack
        self.rear = -1  # rear points to the last element in the stack
        self.count = 0  # current size of the stack
        self.last_pop = None

    def pop(self):
        if self.is_empty():
            return False
        value = self.s[self.rear]
        self.rear = (self.rear - 1) % self.capacity
        self.count = self.count - 1
        self.last_pop = value
        return value

    def append(self, value):
        if self.is_full():
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.s[self.rear] = value
        self.count = self.count + 1
        return True

    def peek(self):
        if self.is_empty():
            return False
        return self.s[self.rear]

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

    def sort(self):
        new = []
        i = 0
        for s in range(self.count):
            new.append(self.s[i])
            i += 1
        new.sort()
        for s in range(self.capacity - self.count):
            new.append([None])
        self.s = new

    def print(self):
        result = []
        i = 0
        for s in range(self.count):
            result.append(f'<{self.s[i%self.capacity]}>')
            i += 1
        for s in range(self.capacity - self.count):
            result.append('<_>')
        result.reverse()
        string = ""
        for s in result:
            string += f'{s} '
        return string

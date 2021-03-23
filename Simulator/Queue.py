class Queue:

    # Initialize queue
    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = 0  # front points to the front element in the queue
        self.rear = -1  # rear points to the last element in the queue
        self.count = 0  # current size of the queue
        self.last_pop = None

    # Function to dequeue the front element
    def pop(self):
        # check for queue underflow
        if self.is_empty():
            return False
        value = self.q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        self.last_pop = value
        return value

    # Function to add an element to the queue
    def append(self, value):
        # check for queue overflow
        if self.is_full():
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1
        return True

    # Function to return the front element of the queue
    def peek(self):
        if self.is_empty():
            return False
        return self.q[self.front]

    # Function to return the size of the queue
    def size(self):
        return self.count

    # Function to check if the queue is empty or not
    def is_empty(self):
        return self.size() == 0

    # Function to check if the queue is full or not
    def is_full(self):
        return self.size() == self.capacity

    def sort(self):
        new = []
        i = self.front
        for q in range(self.count):
            new.append(self.q[i % self.capacity])
            i += 1
        new.sort()
        for q in range(self.capacity - self.count):
            new.append([None])
        self.front = 0
        self.rear = self.count-1
        self.q = new

    def print(self):
        result = []
        i = self.front
        for q in range(self.count):
            result.append(f'<{self.q[i%self.capacity]}>')
            i += 1
        for q in range(self.capacity - self.count):
            result.append('<_>')
        result.reverse()
        string = ""
        for q in result:
            string += f'{q} '
        return string


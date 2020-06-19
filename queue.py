# !python3

class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity




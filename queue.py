# !python3

class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity

    def qFull(self):
        return self.size == self.capacity

    def qEmpty():
        return self.size == 0

# !python3

class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity

    def qFull(self):
        return self.size == self.capacity

    def qEmpty(self):
        return self.size == 0

    # Function to add an item into the queue
    def enqueue(self, item):
        if self.qFull():
            print("Warning: the queue is full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item 
        self.size = self.size + 1
        print("% s has been enqueued" % str(item))

if __name__ == "__main__":
    queue = Queue(30)
    queue.enqueue(10)

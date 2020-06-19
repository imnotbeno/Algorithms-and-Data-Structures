# !python3

# A fifo queue
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
            print("Warning: Queue is full, cannot add more items.")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item 
        self.size = self.size + 1
        print("% s has been enqueued" % str(item))

    # Function to remove an item from queue
    def dequeue(self):    
        if self.qEmpty():
            print("Warning: Queue is empty, nothing to remove.")
            return

        print("% s dequeue from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

if __name__ == "__main__":
    queue = Queue(30)
    queue.enqueue(10)

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

    # Function to get rear element
    def getRear(self):
        if self.qEmpty():
            print("The queue is empty!")
        print("The rear element of the queue is: ", self.Q[self.rear])

    # Function to get front element
    def getFront(self):
        if self.qEmpty():
            print("The queue is empty!")
        print("The front element of the queueu is: ", self.Q[self.front])

if __name__ == "__main__":
    queue = Queue(30)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(50)
    queue.enqueue(40)
    queue.dequeue()
    queue.getFront()
    queue.getRear()
    # All these operations need O(1) time


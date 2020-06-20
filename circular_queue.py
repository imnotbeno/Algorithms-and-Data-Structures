# !python3
# Circular queue array implementation

# initializing the class
class CircularQueue():

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    # Function to insert item into queue
    def enqueue(self, item):
        
        # Check if queue is full 
        if(self.rear + 1) % self.size == self.front:
            print("Queue is full!")

        # Empty queue
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    # Function to delete item in queue
    #def dequeue(self):    
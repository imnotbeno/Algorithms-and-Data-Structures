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
            print("% s has been enqueued!")

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    # Function to delete item in queue
    def dequeue(self):    
        if self.front == -1:
            print("Queue is empty!")

        # Condition for only one element
        elif self.front == self.rear:
            tmp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return tmp

        else:
            tmp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return tmp

    # Function to display the queue
    def display(self):
        
        if self.front == -1:
            print("The queue is empty!")

        elif self.rear >= self.front:
            print("Elements in circular queue are: ", end=" ")

            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Elements in circular queue are: ", end=" ")

            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")


# Driver code
if __name__ == "__main__":
    cq = CircularQueue(40)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(35)
    cq.enqueue(52)
    cq.display()
    cq.dequeue()
    cq.display()
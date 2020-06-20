# !python3
# Circular queue array implementation

# initializing the class
class CircularQueue():

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  #Assign data
        self.next = None  #Initialize next as null


# Linked list class with one node object
class LinkedList:

    def __init__(self):
        self.head = None

    # Adding the new node in front - O(1) time complexity
    def front(self, new):
        new_node = Node(new)  # Allocate the node and put in the data
        new_node.next = self.head  # Make next of new Node as head
        self.head = new_node  # Move the head to point to new Node

    # Adding a new node after a given node - O(1) time complexity
    def insert(self, new, prev_node):

        if prev_node is None:
            print("Previous node does not exist")
            return

        new_node = Node(new)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Adding in the end - O(n) time complexity, where n is the number of nodes
    def append(self, new):
        new_node = Node(new)

        # Check if the list is empty
        if self.head is None:
            self.head = new_node
            return

        # If it is not, traverse through until the last node
        last = self.head
        while last.next:
            last = last.next

        # Change the next of last node
        last.next = new_node

    # Traversing through and printing the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.head = Node(3)
    second = Node(1)
    third = Node(8)

    linked_list.head.next = second
    second.next = third

    linked_list.front(9)
    linked_list.append(5)
    #linked_list.insert(linked_list.head.next, 7)

    linked_list.print_list()



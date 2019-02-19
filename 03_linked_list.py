class Node:
    def __init__(self, data):
        self.data = data # Assign the data here
        self.next = None # Set next to None by default.


class LinkedList:
    def __init__(self):
        self.head = None

    # Display the list. Linked list traversal.
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, data):
        # Create the new node before we insert it at the beginning of the LL
        new_node = Node(data)

        # Assign the next pointer to the head
        new_node.next = self.head

        # Move the head pointer to the new node.
        self.head = new_node


# Tests

# Initialize linked list
llist = LinkedList()

# Create some nodes.
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.display()


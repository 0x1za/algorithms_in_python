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
        display = ""
        while temp:
            display+=(str(temp.data)+" -> ")
            temp = temp.next
        display+="None"
        print(display)

    def push(self, data):
        # Create the new node before we insert it at the beginning of the LL
        new_node = Node(data)

        # Assign the next pointer to the head
        new_node.next = self.head

        # Move the head pointer to the new node.
        self.head = new_node

    def append(self, data):
        # Inserting data at the end of the linked list.

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


    def insert(self, previous_node, data):
        if previous_node == None:
            return

        # Create a new node with new data
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node


# Tests

# Initialize linked list
llist = LinkedList()

# Create some nodes.
llist.push(2)
llist.push(3)
llist.push(4)

llist.append(1)

llist.display()


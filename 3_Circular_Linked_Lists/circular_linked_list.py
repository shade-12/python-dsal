class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None

    def __len__(self):
        """
        Calculate length of circular linked list.
        """
        if not self.head:
            return 0
        if self.head == self.head.next:
            return 1
        curr, count = self.head, 0
        while curr.next != self.head:
            curr = curr.next
            count += 1
        return count

    def print_list(self):
        """
        Print all elements in circular linked list starting from head.
        """
        node = self.head
        while node:
            end = None if node.next == self.head else " -> "
            print(node.data, end=end)
            node = node.next
            if node == self.head:
                break
    
    ########## START: INSERTION ##########

    def append(self, data):
        """
        Append new node at the end of circular linked list.
        """
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            new_node.next = new_node
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        # Found last node before getting back to head again
        new_node = Node(data)
        new_node.next = self.head
        curr.next = new_node

    def prepend(self, data):
        """
        Prepend new node at the head of circular linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            new_node.next = self.head
            self.head = new_node
            curr.next = new_node

    ########## END: INSERTION ##########

    ########## START: REMOVE NODE ##########

    def remove(self, key):
        """
        Remove node with data = key from the circular linked list.
        Assume that all elements are unique.
        """
        if not self.head:
            return

        # Case 1: Node to be removed is head node
        curr = self.head
        if curr.data == key:
            # Find the last node before head
            while curr.next != self.head:
                curr = curr.next
            # Only one element in the circular linked list
            if self.head == self.head.next:
                self.head = None
            else:
                curr.next = self.head.next
                self.head = curr.next
        else:
            # Case 2: Node to be removed is not head node
            prev = None
            while curr.next != self.head:
                if curr.data == key:
                    prev.next = curr.next
                    curr = None
                    return
                prev = curr
                curr = curr.next

    ######### END: REMOVE NODE ##########

    ######### START: SPLIT LINKED LIST INTO TWO HALVES ##########

    def split(self, k):
        length = len(self)
        

    ######### END: SPLIT LINKED LIST INTO TWO HALVES ##########

cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")

cllist.remove("A")
cllist.remove("C")
cllist.print_list()


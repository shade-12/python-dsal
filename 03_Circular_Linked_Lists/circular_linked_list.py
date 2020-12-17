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
        curr, count = self.head, 1
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

    def split(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        curr = self.head

        prev, head2 = None, self.head
        count = 0
        while count < mid:
            prev = head2
            head2 = head2.next
            count += 1
        prev.next = self.head

        second_list = CircularLinkedList()
        # Find last node in the cycle list
        curr = head2
        while curr.next != self.head:
            second_list.append(curr.data)
            curr = curr.next
        second_list.append(curr.data)
        curr.next = head2

        self.print_list()
        second_list.print_list()

    ######### END: SPLIT LINKED LIST INTO TWO HALVES ##########

    ######## START: JOSEPHUS PROBLEM ##########

    def remove_node(self, node):
        if self.head == node:
            curr = self.head 
            while curr.next != self.head:
                curr = curr.next
            if self.head == self.head.next:
                self.head = None
            else:
                curr.next = self.head.next 
                self.head = self.head.next
        else:
            curr = self.head 
            prev = None
            while curr.next != self.head:
                prev = curr 
                curr = curr.next 
                if curr == node:
                    prev.next = curr.next
                    curr = curr.next

    def josephus_circle(self, step):
        curr = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                curr = curr.next
                count += 1
            nxt = curr.next
            self.remove_node(curr)
            curr = nxt


    ######### END: JOSEPHUS PROBLEM ##########

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)


cllist.josephus_circle(2)
cllist.print_list()

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while node:
            end = None if node.next == self.head else " -> "
            print(node.data, end=end)
            node = node.next
            if node == self.head:
                break
    
    ########## START: INSERTION ##########

    def append(self, data):
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

cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")

cllist.remove("A")
cllist.remove("C")
cllist.print_list()


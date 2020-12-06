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


cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            end = None if not curr.next else " -> "
            print(curr.data, end=end)
            curr = curr.next
    
    ########## START: APPEND/PREPEND ##########

    def append(self, data):
        """
        Insert new node at the end of linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        
    def prepend(self, data):
        """
        Insert new node at the head of linked list.
        """
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    ########## END: APPEND/PREPEND ##########

    ########## START: INSERT NODE ##########

    def add_after_node(self, key, data):
        """
        Insert new node after the node where node.data = key.
        Assume elements within linked list are unique.
        """
        if not self.head:
            return
        curr = self.head
        while curr:
            if curr.data == key:
                new_node = Node(data)
                new_node.next = curr.next
                new_node.prev = curr
                curr.next = new_node
                if new_node.next:
                    new_node.next.prev = new_node
                return
            curr = curr.next

    def add_before_node(self, key, data):
        """
        Insert new node before the node where node.data = key.
        Assume elements within linked list are unique.
        """
        if not self.head:
            return
        if self.head.data == key:
            self.prepend(data)
            return
        curr = self.head
        while curr:
            if curr.data == key:
                new_node = Node(data)
                new_node.next = curr
                new_node.prev = curr.prev
                curr.prev = new_node
                if new_node.prev:
                    new_node.prev.next = new_node
                return
            curr = curr.next

    ########## END: INSERT NODE ##########


dllist = DoublyLinkedList()

dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.add_after_node(4,6)
dllist.add_before_node(5,9)

dllist.print_list()
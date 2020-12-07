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
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    ########## END: APPEND/PREPEND ##########


dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.print_list()
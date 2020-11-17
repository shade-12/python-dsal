class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            end = None if cur_node.next is None else " -> "
            print(cur_node.data, end = end)
            cur_node = cur_node.next

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = Node(data)

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.prepend("X")
llist.insert_after(llist.head.next.next, "Y")
llist.delete_node("B")


llist.print_list()  
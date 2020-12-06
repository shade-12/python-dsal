class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            end = None if curr_node.next is None else " -> "
            print(curr_node.data, end=end)
            curr_node = curr_node.next

    ########## START: INSERTION ##########

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    ########## END: INSERTION ##########

    ########## START: DELETION BY VALUE ##########

    def delete_node(self, key):
        tmp = self.head
        # Node to remove is head node
        if tmp and tmp.data == key:
            self.head = self.head.next
            tmp = None
            return
        # Node to remove is not head node
        prev = None
        while tmp.next:
            if tmp.data == key:
                prev.next = tmp.next
                tmp = None
                return
            prev = tmp
            tmp = tmp.next

    ########## END: DELETION BY VALUE ##########

    ########## START: DELETION BY POSITION ##########

    def delete_node_at_pos(self, pos):
        if pos < 0 or self.head is None:
            return

        tmp = self.head
        # Node to remove is at position 0
        if  pos == 0:
            self.head = self.head.next
            tmp = None
            return
        # Node to remove is not at position 0
        prev = None
        count = 0
        while tmp.next:
            if count == pos:
                prev.next = tmp.next
                tmp = None
                return
            prev = tmp
            tmp = tmp.next
            count += 1

    ########## END: DELETION BY POSITION ##########

    ########## START: LENGTH ##########

    def len_iterative(self):
        curr_node, count = self.head, 0
        while curr_node:
            curr_node = curr_node.next
            count += 1
        return count

    def len_recursive(self, node):
        if not node:
            return 0
        return 1 + self.len_recursive(node.next)


    ########## END: LENGTH ##########


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.delete_node("B")
llist.delete_node("E")
llist.delete_node_at_pos(1)
llist.delete_node_at_pos(1)
print(llist.len_recursive(llist.head))

llist.print_list()
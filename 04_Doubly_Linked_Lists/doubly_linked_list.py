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

    ########## START: DELETE NODE ##########
    
    def delete_key(self, key):
        """
        Remove a node where node.data = key from linked list.
        """
        if not self.head:
            return

        if self.head.data == key:
            # Case 1: Remove the only node from the list
            if not self.head.next:
                self.head = None
            # Case 2: Remove head node
            else:
                new_head = self.head.next
                new_head.prev = None
                self.head = None
                self.head = new_head
            return

        # Case 3: Remove node where node.next is not None
        curr = self.head.next
        while curr.next:
            if curr.data == key:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.next, curr.prev = None, None
                curr = None
                return
            curr = curr.next

        # Case 4: Remove node where node.next is None
        if curr.data == key:
            curr.prev.next = None
            curr.next, curr.prev = None, None
            curr = None
        return

    def delete_node(self, node):
        """
        Remove node from linked list if node exist in the list.
        """
        if not self.head:
            return

        if self.head == node:
            # Case 1: Remove the only node from the list
            if not self.head.next:
                self.head = None
            # Case 2: Remove head node
            else:
                new_head = self.head.next
                new_head.prev = None
                self.head = None
                self.head = new_head
            return

        # Case 3: Remove node where node.next is not None
        curr = self.head.next
        while curr.next:
            if curr == node:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.next, curr.prev = None, None
                curr = None
                return
            curr = curr.next

        # Case 4: Remove node where node.next is None
        if curr == node:
            curr.prev.next = None
            curr.next, curr.prev = None, None
            curr = None
        return

    ########## END: DELETE NODE ##########

    ########## START: REVERSE ##########

    def reverse(self):
        """
        Reverse doubly linked list.
        """
        # Return if linked list has length < 2
        if not self.head or not self.head.next:
            return

        curr = self.head
        while curr.next:
            nxt = curr.next
            curr.next, curr.prev = curr.prev, curr.next
            curr = nxt
        curr.next, curr.prev = curr.prev, curr.next
        self.head = curr

    ########## END: REVERSE ##########

    ########## START: REMOVE DUPLICATES ##########

    def remove_duplicates(self):
        """
        Remove all duplicates from doubly linked list.
        """
        # Return if linked list has length < 2
        if not self.head or not self.head.next:
            return

        store = set()
        curr = self.head
        while curr:
            if not curr.data in store:
                store.add(curr.data)
                curr = curr.next
            else:
                nxt = curr.next
                self.delete_node(curr)
                curr = nxt
            

    ########## END: REMOVE DUPLICATES ##########

    ########## START: PAIRS WITH SUMS ##########

    def pairs_with_sum(self, sum_val):
        """
        Find all pairs(in order) from the linked list that adds up to sum_val.
        """
        if not self.head:
            return list()

        curr = self.head
        store, result = dict(), list()
        while curr:
            if curr.data in store:
                # Found a pair
                result.append([sum_val - curr.data, curr.data])
                store[curr.data] -= 1
                if store[curr.data] == 0:
                    del store[curr.data]
            else:
                val = sum_val - curr.data
                if val in store:
                    store[val] += 1
                else:
                    store[val] = 1
            curr = curr.next
        return result

    ########## START: PAIRS WITH SUMS ##########


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.reverse()
dllist.print_list()
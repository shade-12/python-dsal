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

    def length(self, node):
        if not node:
            return 0
        return 1 + self.length(node.next)

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

    def delete_node_at_pos(self, pos):
        if pos >= self.length(self.head):
            return

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None

        prev_node = None
        count = 0
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def swap_nodes(self, key1, key2):
        if (key1 == key2):
            return
        
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def reverse_iterative(self):
        if self.length(self.head) < 2:
            return

        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev
            nxt = curr.next
            curr.next = prev
            return _reverse_recursive(nxt, curr)

        self.head = _reverse_recursive(curr=self.head, prev=None)
        
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        r = None

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                r = p
                p = p.next
            else:
                r = q
                q = q.next
            new_head = r
        while p and q:
            if p.data <= q.data:
                r.next = p
                r = p
                p = p.next
            else:
                r.next = q
                r = q
                q = q.next
        # One of the list has reached the end
        if not p:
            r.next = q
        if not q:
            r.next = p
        return new_head

    def remove_duplicates(self):
        curr = self.head
        prev = None
        values = set()

        while curr:
            if curr.data in values:
                # Remove curr node
                prev.next = curr.next
                curr = None
            else:
                # Add to set
                values.add(curr.data)
                prev = curr
            curr = prev.next

    def print_nth_from_last(self, n):
        len = self.length(self.head)
        if (n > len):
            return
        curr = self.head

        while curr:
            if len == n:
                print(curr.data)
                return curr.data
            len -= 1
            curr = curr.next
        if not curr:
            return

    def count_occurences_iterative(self, data):
        count = 0
        curr = self.head
        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if k > self.length(self.head):
            return

        p = self.head
        q = self.head
        prev = None
        count = 0
        # Find pivot node
        while p and count < k:
            prev = p
            p, q = p.next, q.next
            count += 1
        # Found pivot node
        p = prev
        # Find last node
        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    '''
    Move the tail of a linked list to head.
    '''
    def move_tail_to_head(self):
        # Return if linked list has length is less than 2
        if not self.head or not self.head.next:
            return
        
        prev = None
        tail = self.head
        # Find the tail node
        while tail.next:
            prev = tail
            tail = tail.next
        prev.next = None
        tail.next = self.head
        self.head = tail


llist = LinkedList()
llist.append("A")
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("X")
llist.insert_after(llist.head.next.next, "Y")
llist.swap_nodes("C", "D")

print(llist.length(llist.head))
print("Original list: ", end="")
llist.print_list()

llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes: ", end="")
llist.print_list()

llist.swap_nodes("X", "B")
print("Swapping nodes X and B where key_1 is head node: ", end="")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node: ", end="")
llist.print_list()

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same: ", end="")
llist.print_list()

llist.reverse_iterative()
print("Reversed(iterative) list: ", end="")
llist.print_list()

llist.reverse_recursive()
print("Reversed(recursive) list: ", end="")
llist.print_list()

count = llist.count_occurences_recursive(llist.head, "A")
print("No of occurences of A: ", count)

llist.rotate(3)
print("Rotated: ", end="")
llist.print_list()
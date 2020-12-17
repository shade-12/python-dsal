from queue import Queue
from stack import Stack

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    ########## START: PRE-ORDER TRAVERSAL ##########
    
    def preorder_print(self, start, traversal_str):
        if start:
            traversal_str += (str(start.value) + "-")
            traversal_str = self.preorder_print(start.left, traversal_str)
            traversal_str = self.preorder_print(start.right, traversal_str)
        return traversal_str

    ########## END: PRE-ORDER TRAVERSAL ##########

    ########## START: IN-ORDER TRAVERSAL ##########

    def inorder_print(self, start, traversal_str):
        if start:
            traversal_str = self.inorder_print(start.left, traversal_str)
            traversal_str += (str(start.value) + "-")
            traversal_str = self.inorder_print(start.right, traversal_str)
        return traversal_str

    ########## END: IN-ORDER TRAVERSAL ##########

    ########## START: POST-ORDER TRAVERSAL ##########

    def postorder_print(self, start, traversal_str):
        if start:
            traversal_str = self.postorder_print(start.left, traversal_str)
            traversal_str = self.postorder_print(start.right, traversal_str)
            traversal_str += (str(start.value) + "-")
        return traversal_str

    ########## END: POST-ORDER TRAVERSAL ##########

    ########## START: LEVEL-ORDER TRAVERSAL ##########

    def levelorder_print(self, start):
        if not start:
            return

        q = Queue()
        q.enqueue(start)
        traversal = ""

        while not q.is_empty():
            ele = q.dequeue()
            traversal += str(ele.value) + "-"
            if ele.left is not None:
                q.enqueue(ele.left)
            if ele.right is not None:
                q.enqueue(ele.right)

        return traversal

    ########## END: LEVEL-ORDER TRAVERSAL ##########

    ########## START: REVERSE LEVEL-ORDER TRAVERSAL ##########

    def reverse_levelorder_print(self, start):
        if not start:
            return

        s = Stack()
        q = Queue()
        q.enqueue(start)
        traversal = ""

        while not q.is_empty():
            ele = q.dequeue()
            s.push(ele.value)
            # Add right node to queue first
            if ele.right is not None:
                q.enqueue(ele.right)
            if ele.left is not None:
                q.enqueue(ele.left)
        
        while not s.is_empty():
            traversal += str(s.pop()) + "-"
        return traversal

    ########## END: REVERSE LEVEL-ORDER TRAVERSAL ##########

    ########## START: HEIGHT OF TREE ##########

    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    ########## END: HEIGHT OF TREE ##########

    ########## START: SIZE OF TREE ##########

    def tree_size(self, node):
        """
        Number of nodes in tree.
        """
        if not node:
            return 0
        return 1 + self.tree_size(node.left) + self.tree_size(node.right)

    ########## END: SIZE OF TREE ##########


# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# print(tree.print_tree("preorder"))
# print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("reverse_levelorder"))
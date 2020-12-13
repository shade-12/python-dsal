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
print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))
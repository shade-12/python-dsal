import math

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    ########## START: INSERTION ##########

    def insert(self, new_val):
        """
        Insert a new value into BST.
        """
        def _insert_recursive(node, new_val):
            if new_val < node.data:
                if node.left:
                    _insert_recursive(node.left, new_val)
                else:
                    node.left = Node(new_val)
            else:
                if node.right:
                    _insert_recursive(node.right, new_val)
                else:
                    node.right = Node(new_val)

        _insert_recursive(self.root, new_val)

    ########## END: INSERTION ##########

    ########## START: SEARCH ##########

    def search(self, find_val):
        """
        Find value in BST. Return True if value exist, otherwise False.
        """
        def _find_recursive(node, find_val):
            if not node:
                return False
            if find_val == node.data:
                return True
            elif find_val < node.data:
                return _find_recursive(node.left, find_val)
            else:
                return _find_recursive(node.right, find_val)
            

        return _find_recursive(self.root, find_val)

    ########## END: SEARCH ##########

    ######### START: CHECK BST PROPERTY ##########

    def is_bst(self):
        """
        Check if a tree is a BST.
        Definition: 
        The BST property states that every node on the right subtree has to be larger than the current node, 
        and every node on the left subtree has to be smaller than the current node.
        """
        def _is_bst_recursive(node, max_val=math.inf, min_val=-math.inf):
            if not node:
                return True
            if node.data <= min_val or node.data >= max_val:
                return False
            else:
                left = _is_bst_recursive(node.left, node.data, min_val)
                right = _is_bst_recursive(node.right, max_val, node.data)
                return left and right

        return _is_bst_recursive(self.root)

    ######### END: CHECK BST PROPERTY ##########


bst = BST(7)
bst.insert(3)
bst.insert(10)
bst.insert(5)
bst.insert(1)
bst.insert(8)
bst.insert(9)
bst.insert(2)

bst.inorder_print_tree()      
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

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


bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))
print(bst.search(1))
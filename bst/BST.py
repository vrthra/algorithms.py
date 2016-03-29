import doctest

class Node():
    """
    >>> n = Node(100)
    >>> n
    Node: [100, None, None]
    """
    def __init__(self, value):
        self.value, self.right, self.left = value, None, None
    def __repr__(self):
        return "Node: %s" % self.preorder()

    def preorder(self):
        l = self.left if self.left else None
        r = self.right if self.right else None
        a = [self.value, l, r]
        return a

    def inorder(self):
        l = self.left if self.left else None
        r = self.right if self.right else None
        a = [l, self.value, r]
        return a


class BST():
    """
    >>> tree = BST()
    >>> for i in [4, 2, 6, 1, 3, 7, 5]: tree.insert(i)
    >>> tree
    BST: [Node: [2, Node: [1, None, None], Node: [3, None, None]], 4, Node: [6, Node: [5, None, None], Node: [7, None, None]]]
    """
    def __init__(self): self.root = None

    def __repr__(self): return 'BST: ' + (str(self.root.inorder()) if self.root else 'None')

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            cur = self.root
            while True:
                if value < cur.value:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(value)
                        break
                elif value > cur.value:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(value)
                        break
                else:
                    break



if __name__ == '__main__': doctest.testmod()
# tree = BST()
# for i in [4, 2, 6, 1, 3, 7, 5]: tree.insert(i)
# print(tree)


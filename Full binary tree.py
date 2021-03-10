class Node:
    def __init__(self , item):
        self.right = None
        self.left = None
        self.val = item

    def perfect(self):
        if self.val is None:
            return True

        elif self.left is None and self.right is None:
            return True

        elif self.left is None and self.right != None or self.right is None and self.left != None:
            return False
        else:
            return self.left.perfect() and self.right.perfect()   

root = Node(1)
root.left = Node(12)
root.right = Node(9)
root.right.left = Node(13)
root.left.left = Node(5)
root.left.right = Node(6)

print(root.perfect())
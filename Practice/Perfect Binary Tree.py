class Node:
    def __init__(self , item):
        self.right = None
        self.left = None
        self.val = item

    def depth(self):
        dep = 0
        refer = self.left
        while refer is not None:
            dep += 1
            refer = refer.left
        return dep 

    def perfecttree(self,dep,level = 0 ):
        if self.val is None:
            return True
        elif self.left is None and self.right is None:
            return (dep == level + 1 )
        elif self.left is None or self.right is None:
            return False
        else:
            return (self.left.perfecttree( dep , level + 1) and self.right.perfecttree(dep , level + 1))

root = Node(1)
root.left = Node(12)
root.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.left.left = Node(5)
root.left.right = Node(6)
# root.left.left.left = Node(15)

print(root.perfecttree(3))


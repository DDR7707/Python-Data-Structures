class Node:
    def __init__(self , val):
        self.val = val
        self.right = None
        self.left = None


def leftview(root):
    if not root:
        return

    final = [root.val]
    que = [root]

    while que:
        temp = []
        for i in que:
            if i.left:
                temp.append(i.left)

            if i.right:
                temp.append(i.right)    
        if temp:
            final.append(temp[0].val)        

        que = temp

    return final

def rightview(root):
    if not root:
        return

    final = [root.val]
    que = [root]

    while que:
        temp = []
        for i in que:
            if i.left:
                temp.append(i.left)

            if i.right:
                temp.append(i.right)    
        if temp:
            final.append(temp[-1].val)        

        que = temp

    return final





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.left.right.right = Node(10)
root.right.right.left = Node(14)
print("Left view  : " , leftview(root))
print("Right View :"  , rightview(root))

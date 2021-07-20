class Linkedlist:
    def __init__(self , data):
        self.data = data
        self.next = None


class Tree:
    def __init__(self , val):
        self.val = val
        self.left = None
        self.right = None 

def convert(head):

    if not head:
        return None

    root = Tree(head.data)
    sam = [root]
    head = head.next

    while True:
        re = sam[0]

        if not head:
            break

        re.left = Tree(head.data)
        sam.append(re.left)
        head = head.next 
        
        if not head:
            break

        re.right = Tree(head.data)
        sam.append(re.right)
        head = head.next

        sam.pop(0)
  

    inorder(root)

def ll_printing(head):
    if head == None:
        print("List is empty")
        return

    head = head

    while head:
        print(head.data, end=" --> ")
        head = head.next

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)


head = Linkedlist(1)
head.next = Linkedlist(2)
head.next.next = Linkedlist(3)
head.next.next.next = Linkedlist(4)
head.next.next.next.next = Linkedlist(5)

ll_printing(head)

convert(head)

class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class Binarytree:
    def __init__(self):
        self.head = None
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val , end = " --> ")
            self.inorder(root.right)


    def preorder(self,root):
        if root:
            print(root.val , end = " --> ")
            self.inorder(root.left)
            self.inorder(root.right)


    def postorder(self,root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.val , end = " --> ")


    def insert(self,data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return self
        current = self.head
        while True:
            if current.val > data:
                if current.left == None:
                    current.left =  new
                    return self
                current = current.left
            else:
                if current.right == None:
                    current.right = new
                    return self
                current = current.right

    def breathfirstsearch(self):
        final = []
        queue = []
        cur = self.head
        queue.append(cur)
        while len(queue) > 0:
            cur = queue.pop(0)
            final.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        print(final)


        '''     Inorder transversal  (or)  postorder transversal  (or) 
                preorder transversal  are equal to depthfirstsearch  
        '''

    def depthfirstsearch(self,root):
        cur = root
        if cur:
            self.depthfirstsearch(root.left)
            print(cur.val , end = " --> ")
            self.depthfirstsearch(root.right)




            


bst = Binarytree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.inorder(bst.head)
print("\n")
bst.breathfirstsearch()
print("\n")
bst.depthfirstsearch(bst.head)


'''     

                    Tree transversal quiz

//If you know a solution is not far from the root of the tree:
BFS

//If the tree is very deep and solutions are rare, 
BFS (DFS will take long time. )

//If the tree is very wide:
DFS (BFS will need too much memory)

//If solutions are frequent but located deep in the tree
DFS

//determining whether a path exists between two nodes
DFS

//Finding the shortest path
BFS


'''
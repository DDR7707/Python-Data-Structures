class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
def inorder(root):
        if root:
            inorder(root.left)
            print(root.val , end = "-->")
            inorder(root.right)
    
            
def factorTree(n):
    root = Tree(n)
    
    def rec(root):
        n = root.val
        if n == 2:
            return
        elif n == 3:
            return
        
        for i in range(2,int(n/2)):
            if n%i == 0:
                root.left = Tree(i)
                root.right = Tree(int(n/i))
                return rec(root.left) , rec(root.right)
                
            else:
                continue
   
    rec(root)
    return root            

n = 50
print(inorder(factorTree(n)))

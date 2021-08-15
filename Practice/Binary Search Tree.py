class Node:
    def __init__(self , item):
        self.val = item
        self.right = self.left = None
    
          

class Binarytree:
    def __init__(self):
        self.head = None

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val , end = "-->")
            self.inorder(root.right)    
         

    def insert(self , data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return self    
        current = self.head
        while True:
                # Left
                if data < current.val:
                    if current.left is None:
                        current.left = new
                        return self
                    current = current.left
                # Right
                else :
                    if current.right is None:
                        current.right = new
                        return self
                    current = current.right  

    def lookup(self , tar):
        if self.head is None:
            return False
        current = self.head
        while True:
            if  tar < current.val:
                if current.left is None:
                    return False
                current = current.left
            elif tar == current.val:
                return True # tar
            else:
                if current.right is None:
                    return False
                current = current.right    

    '''     Not completed remove part    '''             

    # def remove(self,num):
    #     if self.head == None:
    #         print("Empty tree given")
    #         return self
    #     current = self.head
    #     prev = None
    #     while True:
    #         if num < current.val:
    #             prev = current
    #             current = current.left
    #         elif num > current.right:
    #             prev = current
    #             current = current.right
    #         else:
    #             # Two children are None
    #             if current.left == None and current.right == None:
    #                 if num < prev.left:
    #                     prev.left = None
    #                     current = None
    #                     return self
    #                 else:
    #                     prev.right = None
    #                     current = None
    #                     return self    
    #             # If left child is None
    #             if current.left == None :
                    






bst = Binarytree()
bst.insert(9)
bst.insert(4)
bst.insert(3)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.inorder(bst.head)



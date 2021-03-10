class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,num):
        if self.head is None:
            self.head = Node(num)
            return self.head
        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = Node(num)
        return self.head

    def printing(self):
        cur = self.head
        while cur:
            print(cur.data , end = " --> ")
            cur = cur.next

    def removeduplicatefromsorted(self):
        cur = self.head.next
        prev = self.head
        while cur:
            if cur.data == prev.data:
                prev.next = cur.next
                cur = None
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return self.head 


    def getNthFromLast(self,n):
        cur = res = self.head
        for i in range(n):
            if res:
                res = res.next
            else:
                return -1
        while res:
            cur = cur.next
            res = res.next
        return cur.data 

    def removeloop(self):
        slow = fast = self.head
        while True:
            slow = slow.next
            fast = fast.next.next

            if slow.data == fast.data:
                break

        slow = self.head
        refer = None
        while slow.data != fast.data:
            refer = slow
            slow = slow.next
            fast = fast.next

        refer.next = None
        
        return self.head 



def intersetPoint(head1,head2):
    cur1 = head1
    cur2 = head2

    if cur1 == None or cur2 == None:
        return -1

    while True:
        cur1 = cur1.next
        cur2 = cur2.next
        
        if cur1 == None:
            cur1 = head2
        if cur2 == None:
            cur2 = head1
        if cur1.data == cur2.data:
            return cur1.data    

def findIntersection(head1,head2):
    #return head
    new = []
    cur1 = head1
    cur2 = head2
    while cur1.next and cur2.next:
        if cur1.data < cur2.data:
            cur1 = cur1.next
        elif cur1.data > cur2.data:
            cur2 = cur2.next
        else:
            new.append(cur2.data)
            cur1 = cur1.data
            cur2 = cur2.data
    return new 


ll = Linkedlist()
ll.insert(2)
ll.insert(3)
ll.insert(6)
ll.insert(1)
ll.insert(5)
ll.insert(6)
# print(ll.removeloop())
ll.printing()
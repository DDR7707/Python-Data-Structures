class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def printing(self):
        if self.head == None:
            print("List is empty")
            return

        head = self.head

        while head:
            print(head.data, end=" --> ")
            head = head.next

    def append(self, data):
        new = Node(data)
        current = self.head

        if current == None:
            self.head = new
            return

        while current.next:
            current = current.next

        current.next = new

    def prepend(self, data):
        new = Node(data)
        if self.head == None:
            print("Theres no linked list")
            self.head = new
            return

        new.next = self.head
        self.head = new

    def insert(self, after_node, data):
        new = Node(data)
        current = self.head

        while current and current.data != after_node:
            current = current.next

        if current is None:
            print("Given node data not found")
            return

        new.next = current.next
        current.next = new

    def insertion_index(self, index, data):
        new = Node(data)
        current = self.head

        for i in range(index):
            if current is None:
                print("Index out of range")
                return
            current = current.next

        new.next = current.next
        current.next = new

    def length(self):
        count = 0
        head = self.head

        while head:
            count += 1
            head = head.next

        print(f"Length of linkedlist is {count}")

    def length_recursion(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursion(node.next)

    def deletion(self, node):
        current = self.head
        prev = None

        if current.data == node:
            self.head = current.next
            current = None
            return

        while current and current.data != node:
            prev = current
            current = current.next

        if current == None:
            print("Given data not found")
            return

        prev.next = current.next
        current = None

    def deletion_by_position(self, position):
        current = self.head
        prev = None

        if position == 0:
            self.head = current.next
            current = None
            return

        for i in range(position):
            if current.next is None:
                print("Deletion out of range")
                return
            prev = current
            current = current.next

        prev.next = current.next
        current = None

    def swapnodes(self, node1, node2):
        current1 = self.head
        prev1 = None
        if node1 == node2:
            return

        while current1 and current1.data != node1:
            prev1 = current1
            current1 = current1.next

        current2 = self.head
        prev2 = None

        while current2 and current2.data != node2:
            prev2 = current2
            current2 = current2.next

        if prev1:
            prev1.next = current2
        else:
            self.head = current2

        if prev2:
            prev2.next = current1

        else:
            self.head = current1

        current1.next, current2.next = current2.next, current1.next

    def occurance(self, reference):
        count = 0
        current = self.head

        while current:
            if current.data == reference:
                count += 1
            current = current.next

        return count

    def rotation(self, node):
        current = self.head
        temp = self.head
        while current.data != node and current:
            current = current.next

        self.head = current.next
        current.next = None
        new = self.head
        while new.next:
            new = new.next

        new.next = temp
        return

    def nth_last_node(self, num):
        current = self.head
        final = {}
        count = 0
        while current:
            final[count] = current.data
            current = current.next
            count += 1

        return final[count - num]

    def nth_last_method2(self, sam):
        p = self.head
        q = self.head
        for i in range(sam):
            q = q.next

        while q != None:
            p = p.next
            q = q.next

        return p.data

    def move_tail_to_head(self):
        current = self.head
        prev = None

        while current.next:
            prev = current
            current = current.next

        current.next = self.head
        prev.next = None
        self.head = current

    def remove_duplicate(self):

        current = self.head
        prev = None
        count = dict()

        while current:
            if current.data not in count:
                count[current.data] = 1
                prev = current

            else:
                prev.next = current.next
                current = None
            current = prev.next
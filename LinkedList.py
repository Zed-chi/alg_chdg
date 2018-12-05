"""
Linked List
- addInTail(self, item)
- find(self, val)
- remove(self, val)
- removeAll(self, val)
- clear(self)
- find_all(self, val)
- insert(self, beforeNode, val)
"""


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        all = []
        node = self.head
        while node != None:
            all.append(node.value)
            node = node.next
        return "{}".format(all)
    
    def get_arr(self):
        all = []
        node = self.head
        while node != None:
            all.append(node.value)
            node = node.next
        return all

    def addInTail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def remove(self, val):
        before = None
        cur = self.head
        after = cur.next
        while cur != None:
            if cur.value == val:
                if before == None:
                    self.head = after
                else:
                    before.next = after
                return 0
            else :
                before = cur
                cur = after
                if cur != None:
                    after = cur.next

    def removeAll(self, val):
        before = self.head
        cur = self.head
        after = cur.next
        while cur != None:
            if cur.value == val:
                before.next = after
                cur = before.next
                if cur != None:
                    after = cur.next
                continue
            before = cur
            cur = after
            if cur != None:
                    after = cur.next

    def clear(self):
        self.head = None
        self.tail = None

    def find_all(self, val):
        all = []
        node = self.head
        while node != None:
            if node.value == val:
                all.append(node)
            node = node.next    
        return all

    def __len__(self):
        count = 0
        node = self.head
        while node != None:
            count += 1
            node = node.next
        return count

    def insert(self, nodeAfter, nodeToInsert):
        node = nodeAfter
        if node != None:
            after = node.next
            nodeToInsert.next = after
            node.next = nodeToInsert
        elif node == None and self.__len__ is 0:
            self.addInTail(self, nodeToInsert)

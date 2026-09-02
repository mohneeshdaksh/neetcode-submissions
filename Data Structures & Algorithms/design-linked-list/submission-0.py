class MyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.count = 0

    def get(self, index: int) -> int:
        if index < self.count and index > -1:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        curr_node = self.head
        for _ in range(self.count):
            curr_node = curr_node.next
        new_node = Node(val)
        new_node.next = curr_node.next
        curr_node.next = new_node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count or index < 0:
            return None
        
        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        next_node = curr_node.next
        new_node = Node(val)
        curr_node.next = new_node
        new_node.next = next_node
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count or index < 0:
            return None

        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next
        self.count -= 1
        
class Node:

    def __init__ (self, val):
        self.val = val
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
class MyQueue:

    def __init__(self):
        self.queue1 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        queue2 = []
        for i in range(len(self.queue1)):
            queue2.append(self.queue1.pop())
        elem = queue2.pop()
        for j in range(len(queue2)):
            self.queue1.append(queue2.pop())
        return elem

    def peek(self) -> int:
        queue2 = []
        for k in range(len(self.queue1)-1, -1, -1):
            queue2.append(self.queue1[k])
        return queue2[-1]

    def empty(self) -> bool:
        return not self.queue1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
from collections import deque
class MyStack:

    def __init__(self):
        self.my_stack = deque()

    def push(self, x: int) -> None:
        self.my_stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.my_stack)-1):
            elem = self.my_stack.popleft()
            self.my_stack.append(elem)
        last_elem = self.my_stack.popleft()
        return last_elem

    def top(self) -> int:
        elem = self.pop()
        self.my_stack.append(elem)
        return elem

    def empty(self) -> bool:
        return len(self.my_stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
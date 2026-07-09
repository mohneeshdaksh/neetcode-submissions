class Solution:
    def decodeString(self, s: str) -> str:
        nums = ["0","1","2","3","4","5","6","7","8","9"]
        stack = []
        for i in s:
            if i == "]":
                st = ""
                mul = ""
                while stack[-1] != "[":
                    st = stack.pop() + st
                stack.pop()
                while stack and stack[-1] in nums:
                    mul = stack.pop() + mul
                stack.append(st * int(mul))
            else:
                stack.append(i)
        return "".join(stack)
class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        curr_stack = []

        for i in s:
            if i in ["(", "{", "["]:
                curr_stack.append(i)
            else:
                if len(curr_stack) == 0 or i != parenthesis[curr_stack[-1]]:
                    return False
                else:
                    curr_stack.pop()
        if curr_stack:
            return False
        else:
            return True
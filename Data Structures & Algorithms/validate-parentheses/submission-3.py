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
                if len(curr_stack) == 0:
                    return False
                if i == parenthesis[curr_stack[-1]]:
                    curr_stack.pop()
                else:
                    return False
        if curr_stack:
            return False
        else:
            return True
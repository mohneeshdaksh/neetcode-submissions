class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth, curr_depth = 0, 0
        for ch in s:
            if ch == "(":
                curr_depth += 1
            elif ch == ")":
                curr_depth -= 1
            max_depth = max(max_depth, curr_depth)
        return max_depth
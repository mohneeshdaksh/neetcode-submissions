# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Depth First Search with Recursion
        # if not root:
        #     return 0
        # left_tree = self.maxDepth(root.left)
        # right_tree = self.maxDepth(root.right)
        # return 1 + max(left_tree, right_tree)


        # Breath First Search - Iterative
        # if not root:
        #     return 0
        # q = deque([root])
        # level = 0
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # DFS - Iterative
        stack = [(root, 1)]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
                res = max(res, depth)
        return res
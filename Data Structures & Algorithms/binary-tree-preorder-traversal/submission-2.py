# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # def preorder_recursion(node):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     preorder_recursion(node.left)
        #     preorder_recursion(node.right)        
        # preorder_recursion(root)
        # return res

        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr.right)
                res.append(curr.val)
                curr = curr.left
            curr = stack.pop()
        return res
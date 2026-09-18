# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        # def postorder_recursion(node):
        #     if not node:
        #         return
        #     postorder_recursion(node.left)
        #     postorder_recursion(node.right)
        #     res.append(node.val)
        # postorder_recursion(root)
        # return res

        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr.left)
                res.append(curr.val)
                curr = curr.right
            curr = stack.pop()
        res.reverse()
        return res
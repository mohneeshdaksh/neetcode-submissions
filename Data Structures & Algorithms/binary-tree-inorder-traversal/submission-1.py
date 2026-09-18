# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        # def inorder_recursion(node):
        #     if not node:
        #         return
        #     inorder_recursion(node.left)
        #     res.append(node.val)
        #     inorder_recursion(node.right)
        # inorder_recursion(root)
        # return res

        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
         
        return res
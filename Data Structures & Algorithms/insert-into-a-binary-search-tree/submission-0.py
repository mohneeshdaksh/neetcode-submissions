# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertVal(root, val):
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                return insertVal(root.left, val)
            elif val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                return insertVal(root.right, val)

        if not root:
            return TreeNode(val)
        insertVal(root, val)
        return root
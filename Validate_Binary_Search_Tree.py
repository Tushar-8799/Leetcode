# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        if arr == list(sorted(set(arr))):
            return True
        return False

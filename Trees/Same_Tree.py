# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if both are null, -> return True
        if not p and not q:
            return True
        # if one of them is null
        if not p or not q:
            return False
        # if value of current node of the tree doesn't match
        if p.val != q.val:
            return False

        # check for left node if both are same
        is_same_for_left = self.isSameTree(p.left, q.left)

        # check for right node if both are same
        is_same_for_right = self.isSameTree(p.right, q.right)

        return is_same_for_left and is_same_for_right

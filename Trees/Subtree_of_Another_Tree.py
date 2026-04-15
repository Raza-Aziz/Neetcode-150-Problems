# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        # If main tree is empty, no subtree match possible
        if not root:
            return False

        # Check if trees match at current node
        if self.same(root, subRoot):
            return True

        # Otherwise, check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, a, b):
        # Both nodes are null → match
        if not a and not b:
            return True

        # One is null OR values differ → not a match
        if not a or not b or a.val != b.val:
            return False

        # Check left and right recursively
        return self.same(a.left, b.left) and self.same(a.right, b.right)

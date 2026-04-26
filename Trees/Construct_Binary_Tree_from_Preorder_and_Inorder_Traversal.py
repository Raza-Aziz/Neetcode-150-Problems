# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root


# Explanation
# If lists are empty → no tree, return None

# First element of preorder is the root

# Find root in inorder to split left and right subtrees

# Left subtree size = index of root in inorder

# Build left subtree using:
# preorder[1 : mid + 1], inorder[:mid]

# Build right subtree using:
# preorder[mid + 1 :], inorder[mid + 1 :]

# Attach left and right to root

# Return root

# Key idea:
# Preorder → gives root
# Inorder → splits left and right

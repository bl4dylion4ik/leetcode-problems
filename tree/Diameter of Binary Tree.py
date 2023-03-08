# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(root) -> int:
        def height(root):
            nonlocal diameter
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            print(left, right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        diameter = 0
        height(root)
        return diameter


print(Solution.diameterOfBinaryTree(TreeNode(val=1,
                                             left=TreeNode(val=2, left=TreeNode(val=4,left=None, right=None),
                                             right=TreeNode(val=5, left=None, right=None)),
                                            right=TreeNode(val=3, left=None, right=None))
))
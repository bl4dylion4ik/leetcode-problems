# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, node: Optional[TreeNode], targetSum: int) -> bool:
        if not node:
            return False

        targetSum -= node.val

        if not node.left and not node.right:
            return targetSum == 0

        return self.hasPathSum(node.left, targetSum) or self.hasPathSum(node.right, targetSum)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = deque([p, q])

        while que:
            p = que.popleft()
            q = que.popleft()

            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            que.append(p.left)
            que.append(q.left)
            que.append(p.right)
            que.append(q.right)

        return True
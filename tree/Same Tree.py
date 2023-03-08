# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
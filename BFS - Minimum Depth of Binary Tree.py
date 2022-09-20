# Minimum depth of Binary Tree
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        cnt = 1
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    if not node.left and not node.right:
                        return cnt
                    q.append(node.left)
                    q.append(node.right)
            cnt += 1

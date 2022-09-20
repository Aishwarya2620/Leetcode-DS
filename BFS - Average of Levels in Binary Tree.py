# Average of Levels in Binary Tree
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            avg = 0
            for i in range(qlen):
                node = q.popleft()
                if node:
                    avg += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if avg is not None:
                res.append(avg / qlen)
        return res

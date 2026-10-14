# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        dfs = []
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if level:
                dfs.append(level)
        return dfs

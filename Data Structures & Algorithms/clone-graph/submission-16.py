"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def clone(node):
            if not node:
                return
            if node not in oldToNew:
                oldToNew[node] = Node(node.val)
                for n in node.neighbors:
                    new_n = clone(n)
                    oldToNew[node].neighbors.append(new_n)
            return oldToNew[node]
        return clone(node)
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
        def cloneDfs(node):
            if not node:
                return node

            if node not in oldToNew:
                oldToNew[node] = Node(node.val)
                if node.neighbors is not None:
                    for n in node.neighbors:
                        new_n = cloneDfs(n)
                        print(new_n)
                        oldToNew[node].neighbors.append(new_n)
            return oldToNew[node]
        return cloneDfs(node)
        
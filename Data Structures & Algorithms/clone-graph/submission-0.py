"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        found = {}

        def cloneNode(node):
            if node is None:
                return
            if node not in found:
                new_node = Node(node.val, [])
                found[node] = new_node
                if node.neighbors is not None:
                    for neighbor in node.neighbors:
                        clone = cloneNode(neighbor)
                        new_node.neighbors.append(clone)
            return found[node]
        
        return cloneNode(node)
                
        
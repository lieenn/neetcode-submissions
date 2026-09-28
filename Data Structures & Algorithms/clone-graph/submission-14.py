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
        def clone(node):
            if node is None:
                return node
            if node not in found:
                found[node] = Node(node.val)
                for neighbor in node.neighbors:
                    new_n = clone(neighbor)
                    found[node].neighbors.append(new_n)

            return found[node]
        return clone(node)


        

            
        
        
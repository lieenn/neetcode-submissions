"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return

        found = {}
        stack = []

        new_node = Node(node.val, [])
        found[node] = new_node
        stack.append(node)

        while len(stack) != 0:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in found:
                    found[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                found[n].neighbors.append(found[neighbor])
        return found[node]

        
            

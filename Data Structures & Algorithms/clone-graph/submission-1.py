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
        stack = []

        stack.append(node)

        if node is None:
            return

        found[node] = Node(node.val, [])

        while len(stack) != 0:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in found:
                    new_node = Node(neighbor.val, [])
                    found[neighbor] = new_node
                    stack.append(neighbor)
                    found[n].neighbors.append(found[neighbor])
                else:
                    found[n].neighbors.append(found[neighbor])

        return found[node]

                
        
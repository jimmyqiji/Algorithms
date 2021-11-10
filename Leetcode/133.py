"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        clones = {}
        
        def helper(node):
            if node in clones:
                return clones[node]
            node_clone = Node(node.val)
            clones[node] = node_clone
            for neighbour in node.neighbors:
                neighbour_clone = helper(neighbour)
                node_clone.neighbors.append(neighbour_clone)
            return node_clone
        
        return helper(node)
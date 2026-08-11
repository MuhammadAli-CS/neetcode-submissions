"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        otn={}
        if not node: return None
        def dfs(node): #cloning nodes with vals and appending to its neighbors after discovering and 
                #cloning them
            if node in otn: return otn[node]
            newnode= Node(node.val)
            otn[node]=newnode
            for neighbor in node.neighbors:
                newnode.neighbors.append(dfs(neighbor))
            return newnode
        return dfs(node)
        

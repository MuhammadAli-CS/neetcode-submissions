# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        quep, queq=deque(), deque()
        quep.append(p)
        queq.append(q)

        while quep and queq:
            nodep= quep.pop()
            nodeq=queq.pop()
            if not nodep and not nodeq: continue
            if not nodeq or not nodep: return False
            if nodep.val!=nodeq.val:
                return False
            quep.append(nodep.right)
            queq.append(nodeq.right)
            quep.append(nodep.left)
            queq.append(nodeq.left)

        
        if queq or quep: 
            return False
        return True
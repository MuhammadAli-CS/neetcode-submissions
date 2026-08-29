# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in order traversal
        res=[]

        def dfs(node):
            nonlocal res
            if not node: return
            
            #left, self, right
            if node.left:
                dfs(node.left)
            if len(res)>=k:
                return
            res.append(node.val)
            
            if node.right:
                dfs(node.right)
        dfs(root)
        return res[-1]        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #do dfs while keeping a max variable. if that node is greater than max in tree till that node increment result by one
        res=0

        def dfs(node, maxv):
            nonlocal res
            if node.val>=maxv:
                res+=1
                maxv=node.val
            if node.left:
                dfs(node.left, maxv)
            if node.right:
                dfs(node.right, maxv)


        dfs(root, root.val)
        return res
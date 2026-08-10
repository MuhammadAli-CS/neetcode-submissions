# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p==root or q==root: return  root
        
        #recursive casese
        #if both roots on opposite side of root then it has to be LCA
        if ((p.val>root.val and q.val<root.val) or (p.val<root.val and q.val>root.val)):
            return root
        elif root.val<p.val and root.val<q.val: #(need to search in right subtree)
            return self.lowestCommonAncestor(root.right, p, q)
        else: return self.lowestCommonAncestor(root.left, p, q)
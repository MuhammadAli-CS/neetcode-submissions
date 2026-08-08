# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        queue=deque([root])
        while queue:
            base=queue.pop()
            base.left, base.right=base.right, base.left
            if base.left:
                queue.append(base.left)
            if base.right: queue.append(base.right)
        return root
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #usebfs
        res=[]
        queue=deque([root])
        #have children in queue
        while queue:
            right=None
            qlen=len(queue)
            for i in range(qlen):
                node=queue.popleft()
                if node:
                    right=node # right will have rightmost at end
                    queue.append(node.left)
                    queue.append(node.right)
            if right:
                res.append(right.val)
        return res
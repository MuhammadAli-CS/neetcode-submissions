# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue= deque([root])
        output=[]
        if not root: return []
        while len(queue)>0:
            numc= len(queue)
            temp=[]
            for i in range(numc):
                node=queue.popleft()
                temp.append(node.val)

                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            
            output.append(temp)
        return output

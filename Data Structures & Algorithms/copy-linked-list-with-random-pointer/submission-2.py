"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        newnodes={None: None}
        cur=head

        while cur:
            newnode=Node(cur.val)
            newnodes[cur]=newnode
            cur=cur.next

        cur=head

        while cur:
            newnodes[cur].next=newnodes[cur.next]
            newnodes[cur].random=newnodes[cur.random]

            cur=cur.next
        
        return newnodes[head]
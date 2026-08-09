# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r= head, head
        prev=None
        for _ in range(n):
            r=r.next
        while r:
            r=r.next
            prev=l
            l=l.next
        if prev==None: return l.next
        prev.next=l.next
        return head
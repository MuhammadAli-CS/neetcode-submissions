# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        parse=head
        z=0
        while parse:
            z+=1
            parse=parse.next

        z=z-n+1
        if z==1: return head.next
        prev=None
        target=head
        for i in range(z-1):
            prev=target
            target=target.next
        prev.next=target.next




        return head
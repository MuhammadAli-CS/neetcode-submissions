# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevnode=None
        currnode=head
        
        while currnode:
            nextptr=currnode.next
            currnode.next=prevnode

            prevnode=currnode
            currnode=nextptr

        head=prevnode
        return head
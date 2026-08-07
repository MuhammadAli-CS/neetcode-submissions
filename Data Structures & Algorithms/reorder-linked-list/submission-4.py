# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
      
               
        nextnode=slow.next
        slow.next=None
        currnode=None
        while nextnode:
            temp=nextnode.next
            nextnode.next=currnode
            currnode=nextnode
            nextnode=temp
        shalf=currnode

        while head and shalf:
            temp1 = head.next
            temp2 = shalf.next

            head.next = shalf
            shalf.next = temp1

            head = temp1
            shalf = temp2


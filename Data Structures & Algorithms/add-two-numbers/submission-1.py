# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        head=res
        carry=0
        while l1 or l2:
            if l1 and l2:
                add=l1.val+l2.val+carry
                l1=l1.next
                l2=l2.next
            elif l1: 
                add=l1.val+carry
                l1=l1.next
            elif l2:
                add=l2.val+carry
                l2=l2.next
            carry=add//10
            tsum=add%10
            new=ListNode(tsum)
            
            
            res.next=new
            res=res.next
            
        if carry: res.next=ListNode(carry)



        return head.next
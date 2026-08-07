# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        index_to_node={}
        parse=head
        i=0
        while parse:
            index_to_node[i]=parse
            parse=parse.next
            i+=1
        #we have a dict mapping of each index to the node it originally was on now

        parse=head
        last=i-1
        first=1
        #use two pointers, one from end of list one from start till they overlap
        while first<=last:
            parse.next=index_to_node[last]
            last-=1
            parse=parse.next
            if first<=last:
                parse.next=index_to_node[first]
                first+=1
                parse=parse.next
        parse.next=None
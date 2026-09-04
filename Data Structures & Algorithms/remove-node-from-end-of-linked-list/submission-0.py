# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        dummy=ListNode()
        size=0
        while curr:
            size+=1
            curr=curr.next

        dummy.next=head
        start=dummy
        count=0
        while count<size-n:
            start=start.next
            count+=1
        start.next=start.next.next
        return dummy.next
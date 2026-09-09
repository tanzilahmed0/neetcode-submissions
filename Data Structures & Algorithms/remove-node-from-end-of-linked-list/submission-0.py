# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We need a dummy node so we have a node before head in case we have to remove it

        dummy = ListNode() 
        dummy.next = head 

        slow, fast = dummy, dummy 

        for i in range(n): 
            fast = fast.next 

        while fast.next: 
            slow = slow.next 
            fast = fast.next 

        slow.next = slow.next.next 

        return dummy.next
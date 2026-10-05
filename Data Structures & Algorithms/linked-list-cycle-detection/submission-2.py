# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # We use fast and slow pointers
        # a slow pointer that moves half as fast as the fast pointer 
        # if they equal each other, there's a cycle, if a slow pointer reaches -1, there's no cycle 
        
        slow, fast = head, head 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 

            if fast == slow: 
                return True 

        return False 
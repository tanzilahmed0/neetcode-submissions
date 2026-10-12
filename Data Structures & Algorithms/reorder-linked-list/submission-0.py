# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Use fast and slow pointers to find the mid point in the linked list 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        
        second = slow.next
        # We're splitting the lists so 
        slow.next = None 
        prev = None 
        # Reverse the second list 
        while second: 
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp
        
        first = head
        second = prev 

        while second: 
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1
            first = temp1 
            second = temp2

        


        
        
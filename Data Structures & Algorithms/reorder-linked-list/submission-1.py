# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # First node, then last node, then the og second node, then second to last node etc 
        # We need to find the mid point of the linked list, we can do that with slow and fast pointers 
        # Our slow pointer starts at head and fast is at head.next, when fast reaches the end, 
        # slow should point to the head of the list 
        # To start from the end of the second linkedlist when reordering, we need to reverse it 
        # so we start from head 6 -> 5 -> 4 
        # Then we need to merge it so while the first linkedlist is still unmerge 
        # We point the head of the first list to head of second and then second to first 
        # 
        # [0, 1, 2, 3] [4->5->6]
        # []

        slow, fast = head, head.next 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        list2 = slow.next 
        slow.next = None 

        prev = None
        curr = list2
        while curr: 
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp 

        # prev is head of new reverse list
        # [None->0->1->2->3] [None->6->5->4]
        first, second = head, prev
        while second: 
            temp1, temp2 = first.next, second.next 

            first.next = second 
            second.next = temp1 
            
            first = temp1 
            second = temp2 
            


        
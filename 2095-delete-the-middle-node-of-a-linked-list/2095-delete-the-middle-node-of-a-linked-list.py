# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
            
        curr = head 
        n = 0
        while curr:
            n += 1
            curr = curr.next
        
        middle = n // 2
        temp = head

        for i in range(middle - 1):
            temp = temp.next
        temp.next = temp.next.next

        return head


        
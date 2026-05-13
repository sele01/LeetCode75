# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head

        #declaring poiters for easy walking
        odd = head
        even = head.next
        even_head = even

        #loop through the list and rearrage the poiters

        while even and even.next:
            #alwalys odd comes after the odd
            odd.next = even.next
            odd = odd.next
            #alwalys the even comes after the odd
            even.next = odd.next
            even = even.next
        #merge the poiters
        odd.next = even_head

        return head



        
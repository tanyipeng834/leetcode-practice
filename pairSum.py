# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first_half = head
        second_half= head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            second_half = second_half.next
        prev = None
        current = second_half
        while current is not None:
            next_node = current.next
            current.next = prev
            prev= current
            current = next_node
        second_half=prev
        max_value =-1
        while second_half and first_half:

            max_value = max(second_half.val +first_half.val,max_value)
            first_half = first_half.next
            second_half = second_half.next
        return max_value
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list: ListNode = ListNode()
        new_list_head: ListNode = new_list
        head = head.next
        merge_sum = 0
        while head:
            if head.val == 0:
                new_list.val = merge_sum
                # Add new node if there is more elements in the original list
                if head.next:
                    new_list.next = ListNode()
                    new_list = new_list.next
                merge_sum = 0
            merge_sum += head.val
            head = head.next
        return new_list_head
                
                
           
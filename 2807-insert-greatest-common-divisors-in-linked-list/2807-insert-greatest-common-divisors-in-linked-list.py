# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        currentNode = head
        while currentNode.next is not None:
            new_val = self.gdc(currentNode.val, currentNode.next.val)
            new_node = ListNode(val=new_val, next=currentNode.next)
            currentNode.next = new_node
            currentNode = currentNode.next.next
        return head

    def gdc(self, a: int, b: int) -> int:
        if(b == 0):
            return abs(a)
        else:
            return self.gdc(b, a % b)
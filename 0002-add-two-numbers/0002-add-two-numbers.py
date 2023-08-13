# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        v1 = self.linkedList2Number(l1)
        v2 = self.linkedList2Number(l2)
        result = self.number2linkedList(str(v1 + v2))
        return result

    # Convert list values to number
    def linkedList2Number(self, l: ListNode) -> int:
        num: str = ''
        while l:
            num = str(l.val) + num
            l = l.next
        return int(num)

    # Convert number to linked list
    def number2linkedList(self, n: str) -> ListNode:
        l: ListNode = ListNode()
        head = l
        while n:
            l.val = n[-1]
            n = n[:-1]
            l.next = ListNode() if n else None
            l = l.next
        return head

    
        
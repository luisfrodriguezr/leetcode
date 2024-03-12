class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {0: front}

        while current is not None:
            prefix_sum += current.val
            prefix_sum_to_node[prefix_sum] = current
            current = current.next

        prefix_sum = 0
        current = front

        while current is not None:
            prefix_sum += current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next

        return front.next 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    h = head
    def remove_dfs(node):
      if node.next is None: return 1
      ni = remove_dfs(node.next)
      if ni == n: node.next = node.next.next
      return ni + 1
    
    if head.next is None: return None
    ni = remove_dfs(head)
    if ni == n: return head.next
    return head
    
        
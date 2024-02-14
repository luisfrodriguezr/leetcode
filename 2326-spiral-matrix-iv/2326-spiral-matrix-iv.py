# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    ans = [[-1] * n for _ in range(m)]
    node = head
    
    r = c = 0
    i = j = 0
    while True:
      
      if i == r and j == c:
        while j < n:
          ans[i][j] = node.val
          j += 1
          node = node.next
          if not node: break
        r += 1
        i += 1
        j -= 1
        
      elif i == r and j == n - 1:
        while i < m:
          ans[i][j] = node.val
          i += 1
          node = node.next
          if not node: break
        n -= 1
        j -= 1
        i -= 1
        
      elif i == m - 1 and j == n - 1:
        while j >= c:
          ans[i][j] = node.val
          j -= 1
          node = node.next
          if not node: break
        m -= 1
        j += 1
        i -= 1
      
      elif i == m - 1 and j == c: 
        while i >= r:
          ans[i][j] = node.val
          i -= 1
          node = node.next
          if not node: break
        c += 1
        j += 1
        i += 1
      
      if not node: break
    
    return ans
          
        
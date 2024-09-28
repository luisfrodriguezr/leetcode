class MyCircularDeque:

    class Node:
      def __init__(self, nxt=None, prev=None, val=0):
        self.nxt = nxt
        self.prev = prev
        self.val = val

    def __init__(self, k: int):
      self.curr_size = 0
      self.max_size = k;
      self.front = None
      self.back = None

    def insertFront(self, value: int) -> bool:
      if self.isFull():
        return False

      if self.isEmpty():
        self.front = MyCircularDeque.Node(nxt=None, prev=None, val=value)
        self.back = self.front
      else:
        self.front.prev = MyCircularDeque.Node(nxt=self.front, prev=None, val=value)
        self.front = self.front.prev

      self.curr_size += 1
      
      return True

    def insertLast(self, value: int) -> bool:
      if self.isFull():
        return False

      if self.isEmpty():
        self.front = MyCircularDeque.Node(nxt=None, prev=None, val=value)
        self.back = self.front
      else:
        self.back.nxt = MyCircularDeque.Node(nxt=None, prev=self.back, val=value)
        self.back = self.back.nxt
      
      self.curr_size += 1

      return True
        

    def deleteFront(self) -> bool:
      if self.isEmpty(): return False

      self.front = self.front.nxt

      self.curr_size -= 1

      return True

    def deleteLast(self) -> bool:
      if self.isEmpty(): return False

      self.back = self.back.prev

      self.curr_size -= 1

      return True
        

    def getFront(self) -> int:
      if self.isEmpty(): return -1
      return self.front.val
        

    def getRear(self) -> int:
      if self.isEmpty(): return -1
      return self.back.val
        

    def isEmpty(self) -> bool:
      return self.curr_size == 0

    def isFull(self) -> bool:
      return self.curr_size == self.max_size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
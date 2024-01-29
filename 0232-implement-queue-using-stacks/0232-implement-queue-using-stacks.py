class MyQueue:

    def __init__(self):
      self.stack1 = list()
      self.stack2 = list()

    def push(self, x: int) -> None:
      self.stack1.append(x)

    def pop(self) -> int:
      while len(self.stack1) != 1:
        self.stack2.append(self.stack1.pop())
      ans = self.stack1.pop()
      while len(self.stack2):
        self.stack1.append(self.stack2.pop())
      return ans


    def peek(self) -> int:
      while len(self.stack1) != 1:
        self.stack2.append(self.stack1.pop())
      ans = self.stack1[-1]
      while len(self.stack2):
        self.stack1.append(self.stack2.pop())
      return ans

    def empty(self) -> bool:
      return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
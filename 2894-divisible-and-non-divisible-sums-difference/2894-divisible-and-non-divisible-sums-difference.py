class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1: int = 0
        num2: int = 0
        for i in range(n):
            integer = i + 1
            if integer%m:
                num1 += integer
            else:
                num2 += integer
        return num1 - num2
        
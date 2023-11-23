class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return self.productDigits(n) - self.sumDigits(n)

    def sumDigits(self, n: int):
        _sum: int = 0

        while n:
            _sum += n % 10
            n = int(n / 10)

        return _sum

    def productDigits(self, n: int):
        product: int = 1

        while n:
            product *= n % 10
            n = int(n / 10)

        return product

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        _sum: int = 0

        for i, num in enumerate(nums):
            _sum += num if self.setBitsEqualsK(i, k) else 0

        return _sum

    def setBitsEqualsK(self, num: int, k: int):
        setBits: int = 0
        response: bool = False

        while num >= 1:
            if num % 2 == 1:
                setBits += 1
            num = int(num / 2)

        if setBits == k:
            response = True

        return response

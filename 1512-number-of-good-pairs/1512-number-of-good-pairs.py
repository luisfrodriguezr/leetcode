class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res: int = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1

        return res

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res: int = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    res += 1  
        return res
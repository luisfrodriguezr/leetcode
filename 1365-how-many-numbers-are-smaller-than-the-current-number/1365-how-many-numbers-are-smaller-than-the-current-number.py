class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(1 if y<x else 0 for y in nums) for x in nums]
        
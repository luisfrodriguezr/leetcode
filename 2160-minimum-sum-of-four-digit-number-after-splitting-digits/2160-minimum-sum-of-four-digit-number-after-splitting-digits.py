class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        while num:
            digit = num % 10
            nums.append(digit)
            num = int(num / 10)
        nums.sort()
        return nums[0] * 10 + nums[2] + nums[1] * 10 + nums[3]

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(map(lambda x: int(x>=target), hours))
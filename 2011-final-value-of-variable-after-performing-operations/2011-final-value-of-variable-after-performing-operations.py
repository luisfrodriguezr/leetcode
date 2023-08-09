class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        compute: List[int] = [
            1 if "++" in operation else -1 for operation in operations
        ]
        return sum(compute)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_map = {}
        remaining = []
        result = []
        for value in arr2:
            count_map[value] = 0
        for value in arr1:
            if value in count_map:
                count_map[value] += 1
            else:
                remaining.append(value)
        remaining.sort()
        for value in arr2:
            for _ in range(count_map[value]):
                result.append(value)
        result.extend(remaining)
        return result 
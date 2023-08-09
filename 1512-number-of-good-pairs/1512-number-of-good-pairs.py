# O(n) solution using hash_map
# Assuming that the number of pairs for n identical numbers is n*(n-1)/2
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res: int = 0
        # Create hashmap to count number of repetitions
        hash_map: dict[int, int] = dict()
        for num in nums:
            # Increase num counter in the hash_map using 0 as default value
            hash_map[num] = hash_map.get(num, 0) + 1
        # Sum hash_map using n*(n-1)/2 as number of pairs for identical numbers
        return sum(map(lambda x: int(x * (x - 1) / 2), hash_map.values()))

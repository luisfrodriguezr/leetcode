class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count = 1
        freq_map = defaultdict(dict)

        for num in nums:
            freq_map[num % k][num] = freq_map[num % k].get(num, 0) + 1

        for fr in freq_map.values():
            prev_num, curr, prev1, prev2 = -k, 1, 1, 0

            for num, freq in sorted(fr.items()):
                skip = prev1  
                if num - prev_num == k:
                    take = ((1 << freq) - 1) * prev2
                else:
                    take = ((1 << freq) - 1) * prev1

                curr = skip + take  
                prev2, prev1 = prev1, curr
                prev_num = num
            total_count *= curr
        return total_count - 1 
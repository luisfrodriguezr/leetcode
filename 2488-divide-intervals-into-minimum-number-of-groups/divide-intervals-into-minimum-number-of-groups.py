class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        range_start = float("inf")
        range_end = float("-inf")
        for interval in intervals:
            range_start = min(range_start, interval[0])
            range_end = max(range_end, interval[1])

        point_to_count = [0] * (range_end + 2)
        for interval in intervals:
            point_to_count[
                interval[0]
            ] += 1  # Increment at the start of the interval
            point_to_count[
                interval[1] + 1
            ] -= 1  # Decrement right after the end of the interval

        concurrent_intervals = 0
        max_concurrent_intervals = 0
        for i in range(range_start, range_end + 1):
            concurrent_intervals += point_to_count[i]
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )

        return max_concurrent_intervals 
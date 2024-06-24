class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)  # Length of the input list
        flip_queue = collections.deque()  # Queue to keep track of flips
        flipped = 0  # Current flip state
        result = 0  # Total number of flips

        for i, num in enumerate(nums):

            if i >= k:
                flipped ^= flip_queue[0]

            if flipped == nums[i]:

                if i + k > n:
                    return -1

                flip_queue.append(1)
                flipped ^= 1  # Toggle the flipped state
                result += 1  # Increment the flip count
            else:
                flip_queue.append(0)

            if len(flip_queue) > k:
                flip_queue.popleft()
        return result 
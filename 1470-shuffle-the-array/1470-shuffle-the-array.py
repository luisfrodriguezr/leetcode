class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list: List[int] = []
        for index in range(n):
            # Add x_i to the new list
            new_list.append(nums[index])
            # Add y_i to the new list
            new_list.append(nums[n + index])
        return new_list
            
        
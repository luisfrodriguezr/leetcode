class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        position_in_section = k & -k

        is_in_inverted_part = ((k // position_in_section) >> 1 & 1) == 1

        original_bit_is_one = (k & 1) == 0

        if is_in_inverted_part:
            return "0" if original_bit_is_one else "1"
        else:
            return "1" if original_bit_is_one else "0"
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        original = []
        # Recover the first element
        original.append(first)
        for i, encoded_num in enumerate(encoded):
            recovered = original[i] ^ encoded_num
            original.append(recovered)
        return original

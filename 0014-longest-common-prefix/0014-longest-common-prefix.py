class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word: str = strs[0]
        prefix: str = ""
        for i, v in enumerate(word):
            for string in strs:
                if prefix + v != string[: i + 1]:
                    return prefix
            prefix += v
        return prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        prefix = ""
        for i, v in enumerate(word):
            for string in strs:
                if prefix+v != string[:i+1]:
                    return prefix
            prefix += v
        return prefix
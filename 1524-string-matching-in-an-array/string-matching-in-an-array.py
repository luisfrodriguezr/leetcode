class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()

        for word in words:
            for another_word in words:
                if word != another_word and word in another_word:
                    ans.add(word)

        return list(ans)
                
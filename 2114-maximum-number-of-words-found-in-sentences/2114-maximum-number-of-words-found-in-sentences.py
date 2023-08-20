class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Return the max number of words in a list of sentences
        # A sentence has 'nspaces+1' words
        space: str = ' '
        return max(sentence.count(space) + 1 for sentence in sentences)
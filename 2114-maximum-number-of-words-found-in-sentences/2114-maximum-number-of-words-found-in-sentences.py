class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        #Return the max number of words in a list of sentences
        #A sentence has 'nspaces+1' number of words
        return max(sentence.count(' ') + 1 for sentence in sentences)
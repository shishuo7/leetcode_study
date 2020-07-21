#  词典中最长的单词
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda x: len(x))
        res = [] 
        for word in words:
            if len(word) == 1 or word[:-1] in res:
                res.append(word)
        min_word = res[-1]
        for word in res:
            if len(word) == len(res[-1]) and word < min_word:
                min_word = word
        return min_word


        
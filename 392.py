# 392. 判断子序列
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                t = t[t.index(c) + 1:]
            else:
                return False
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countA = {}
        countB = {}

        for i in range(len(s)):
            countA[s[i]] = 1 + countA.get(s[i], 0)
            countB[t[i]] = 1 + countB.get(t[i], 0)
        
        return countA == countB
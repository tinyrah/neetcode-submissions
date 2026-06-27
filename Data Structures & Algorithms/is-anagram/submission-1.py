class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count up amount of each character for each string
        # compare both counts
        # Edge case 1: strs are not same length -> FALSE
        # Edge case 2: both empty -> true
    
        countA = {}
        countB = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countA[s[i]] = 1 + countA.get(s[i], 0)
            countB[t[i]] = 1 + countB.get(t[i], 0)
        
        if countA == countB:
            return True
        return False
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in ans:
                ans[tuple(count)] = []
            ans[tuple(count)].append(word)
        return list(ans.values())
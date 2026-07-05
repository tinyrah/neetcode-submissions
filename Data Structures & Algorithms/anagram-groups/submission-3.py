class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for word in strs:
            letter_freq_count = [0] * 26
            for char in word:
                letter_freq_count[ord(char) - ord('a')] += 1
            if tuple(letter_freq_count) not in ans:
                ans[tuple(letter_freq_count)] = []
            ans[tuple(letter_freq_count)].append(word)
        
        return list(ans.values())
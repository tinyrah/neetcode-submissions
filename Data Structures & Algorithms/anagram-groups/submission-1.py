class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            if tuple(freq) not in count:
                count[tuple(freq)] = []
            count[tuple(freq)].append(word)
        
        return list(count.values())
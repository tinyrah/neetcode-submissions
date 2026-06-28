class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        count = {}

        for word in words:
            freq_of_letters = [0] * 26
            for c in word:
                freq_of_letters[ord(c) - ord('a')] += 1
            key = tuple(freq_of_letters)
            if key not in count:
                count[key] = []
            count[key].append(word)
        
        return list(count.values())
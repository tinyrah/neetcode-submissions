class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # psuedo solution:
        # count -> hashmap that contains an array of letter frequency as the key, and a word that shares that same letter frequency
        # so, [1,1,1,0,0...0] would be for strings like 'abc', 'cba', 'bca'. so in the count hashmap we have:
        # [1, 1, 1, 0, 0, ...0]: {'abc', 'cba', 'bca'}
        # So, we have to iterate through the strs and count their letter frequencies.
        # then, we can add that frequency count to our dict.

        count = {}
        # letterCount:word

        for word in strs:
            count_letter_freq = [0] * 26
            for c in word:
                count_letter_freq[ord(c) - ord('a')] += 1
            if tuple(count_letter_freq) not in count:
                count[tuple(count_letter_freq)] = []
            count[tuple(count_letter_freq)].append(word)
        
        return list(count.values())

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs.sort()
        # base = strs[0]
        # res = ""

        # for i, c in enumerate(base):
        #     for word in strs:
        #         if word[i] != c:
        #             return res
        #     res += c
        # return res
        base = strs[0]
        res = ""

        for i, c in enumerate(base):
            for word in strs:
                if i >= len(word) or word[i] != c:
                    return res
            res += c
        return res
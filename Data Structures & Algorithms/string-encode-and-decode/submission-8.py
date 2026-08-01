class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        l = 0
        r = 0
        while r < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            r += 1
            l = r
            r = r + length
            res.append(s[l:r])
            l = r
        return res

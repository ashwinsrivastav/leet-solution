class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = i
        i = 0
        res = []
        max = 0
        last = -1
        while i < len(s):
            max = freq[s[i]]
            while i <= max:
                if max >= freq[s[i]]:
                    i += 1
                else:
                    max = freq[s[i]]
                    i += 1
            res.append(max - last)
            last = max
        return res

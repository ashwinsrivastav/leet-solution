class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lenn=len(part)
        while part in s:
            s=s[:s.find(part)]+s[s.find(part)+lenn:]
        return s

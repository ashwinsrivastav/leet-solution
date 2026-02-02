1class Solution:
2    def checkString(self, s: str) -> bool:
3        return list(s)==sorted(s)
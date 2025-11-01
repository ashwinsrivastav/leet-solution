class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y=s.split()
        return(len(y[-1]))
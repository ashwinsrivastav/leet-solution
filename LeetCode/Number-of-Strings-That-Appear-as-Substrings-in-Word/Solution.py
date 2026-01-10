1class Solution:
2    def numOfStrings(self, patterns: List[str], word: str) -> int:        
3        a=[1 for i in patterns if i in word]
4        return sum(a)
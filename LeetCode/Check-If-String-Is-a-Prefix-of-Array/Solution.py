1class Solution:
2    def isPrefixString(self, s: str, words: List[str]) -> bool:
3        a=""
4        for i in words:
5            a+=i
6            if a==s:
7                return True
8        return False
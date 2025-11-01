class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if len(s)!=len(t):
                return False
            elif s.count(i)==t.count(i):
                pass
            else:
                return False
        else:
            return True
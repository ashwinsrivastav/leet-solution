class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=[]
        for i in magazine:
            a.append(i)
        for i in ransomNote:
            if i in a:
                a.remove(i)
            else:
                return False
        return True
    
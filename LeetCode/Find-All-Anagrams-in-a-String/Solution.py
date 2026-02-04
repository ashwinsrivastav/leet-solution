from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pp=Counter(p);res=[]
        length=len(p)
        for i in range(len(s)-length+1):
            temp=s[i:i+length]
            slider=Counter(temp)
            if pp==slider:
                res.append(i)
        return res
            

    

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counter=[];lenght=len(s);i=0;count=0
        while i<lenght:
            k=s[i]
            while s[i]==k:
                count+=1
                if i<lenght-1:
                    i+=1
                else:
                    i+=1
                    break
            counter.append(count)
            count=0
        res=0
        for i in range(len(counter)-1):
            res+= min(counter[i],counter[i+1])
        return res
            

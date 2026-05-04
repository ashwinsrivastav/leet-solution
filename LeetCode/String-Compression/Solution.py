class Solution:
    def compress(self, chars: List[str]) -> int:
        count=0;res=""
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                count+=1
            else:
                if count==0:
                    res+=chars[i]
                    count=0
                    continue
                res+= chars[i]+ str(count+1)
                count=0
        if count!=0:
            res+=chars[-1]+ str(count+1)
        else:
            res+=chars[-1]
        for i in range(len(res)):
            chars[i]=res[i]
        chars[:]=chars[:len(res)]
        return len(chars)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0;uni=set();max=0;i=0
        while i<len(s):
            if s[i] not in uni:
                uni.add(s[i])
                count+=1
                i+=1
            else:
                index=s.index(s[i])
                s=s[index+1::]
                i=0
                if count>max:
                    max=count
                    uni.clear()
                    uni.add(s[i])
                    count=1
                    i+=1
                else:
                    uni.clear()
                    uni.add(s[i])
                    count=1
                    i+=1
        if count>max:
            max=count
        return max

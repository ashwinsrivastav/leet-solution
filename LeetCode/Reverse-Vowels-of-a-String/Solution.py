class Solution:
    def reverseVowels(self, s: str) -> str:
        vov=['a','e','i','o','u','A','E','I','O','U',];rev=[];j=0;lis=list(s)
        for i in range(len(s)):
            if s[i] in vov:
                rev.insert(0,s[i])
        for i in range(len(s)):
            if s[i] in vov:
                lis[i]=rev[j]
                j+=1
        return ''.join(lis)

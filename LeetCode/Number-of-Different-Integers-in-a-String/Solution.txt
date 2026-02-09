1class Solution:
2    def numDifferentIntegers(self, word: str) -> int:
3        nums='0123456789';a='';num=[]
4        for i in word:
5            if i in nums:
6                a+=i
7                continue
8            if a!='':
9                num.append(int(a))
10            a=''
11        if a!='':
12            num.append(int(a))
13        return len(set(num))
14
15
16
17
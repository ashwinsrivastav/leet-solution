1class Solution:
2    def reverseStr(self, s: str, k: int) -> str:
3        rev = ""
4        count = 0
5        valid = 0
6        res = ""
7        for i in range(len(s)):
8            if valid == 0:
9                rev += s[i]
10                count += 1
11                if count == k:
12                    valid = 1
13                    count = 0
14                    res += rev[::-1]
15                    rev = ""
16            else:
17                rev += s[i]
18                count += 1
19                if count == k:
20                    valid = 0
21                    count = 0
22                    res += rev
23                    rev = ""
24        if valid == 0:
25            res += rev[::-1]
26        else:
27            res += rev
28        return res
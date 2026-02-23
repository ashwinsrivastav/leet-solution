1class Solution:
2    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
3        alph = "abcdefghijklmnopqrstuvwxyz"
4        dic = {}
5        line = 1
6        last = 0
7        for key, value in zip(alph, widths):
8            dic[key] = value
9        for i in s:
10            last += dic[i]
11            if last < 101:
12                pass
13            else:
14                line += 1
15                last = dic[i]
16        return [line, last]
17
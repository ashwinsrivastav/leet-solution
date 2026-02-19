1class Solution:
2    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
3        count=0
4        for i in words:
5            for j in i:
6                if j not in allowed:
7                    break
8            else:
9                count+=1
10        return count
11                    
12
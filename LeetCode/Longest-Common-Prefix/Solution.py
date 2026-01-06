1class Solution:
2    def longestCommonPrefix(self, strs):
3        if not strs:
4            return ""
5
6        prefix = ""
7
8        for i in range(len(strs[0])): 
9            char = strs[0][i]
10            
11            for s in strs[1:]:        
12                if i >= len(s) or s[i] != char:
13                    return prefix     
14
15            prefix += char           
16        return prefix
17        
1class Solution:
2    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
3        matchh=0
4        for i in items:
5            if ruleKey=="color" and  ruleValue==i[1]:
6                matchh+=1
7            elif ruleKey == "type" and ruleValue==i[0]:
8                matchh+=1
9            elif ruleKey == "name" and ruleValue==i[2]:
10                matchh+=1
11        return matchh
12
13
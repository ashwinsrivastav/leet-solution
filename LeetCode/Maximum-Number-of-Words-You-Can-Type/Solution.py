1class Solution:
2    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
3        broken=set(brokenLetters)
4        text=text.split()
5        count=len(text)
6        for i in text:
7            for j in broken:
8                if j in i:
9                    count-=1
10                    break
11        return count
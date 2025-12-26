1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        if target not in letters:
4            letters.append(target)
5            letters.sort()
6            if letters[letters.index(target)]==letters[-1]: return letters[0]
7            return letters[letters.index(target)+1]
8        else:
9            letters=letters[::-1]
10            a=letters.index(target)
11            return letters[a-1]
12        
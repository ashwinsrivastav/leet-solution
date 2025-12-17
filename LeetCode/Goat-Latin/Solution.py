1class Solution:
2    def toGoatLatin(self, sentence: str) -> str:
3        sen=sentence.split()
4        vowel=set(['a','e','i','o','u','A','E','I','O','U'])
5        for i,ind in zip(sen,range(len(sen))):
6            if i[0] in vowel:
7                sen[ind]=i+"ma"+"a"*(ind+1)
8            else:
9                prefix=i.removeprefix(i[0])
10                sen[ind]=prefix+i[0]+"ma"+"a"*(ind+1)
11        return " ".join(sen)
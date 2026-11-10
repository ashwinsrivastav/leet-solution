class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        maxx=0
        for i in strs:
            if i.isalpha():
                if len(i)>maxx:
                    maxx=len(i)
            elif i.isdigit():
                if int(i)>maxx:
                    maxx=int(i)
            else:
                if len(i)>maxx:
                    maxx=len(i)
        return maxx

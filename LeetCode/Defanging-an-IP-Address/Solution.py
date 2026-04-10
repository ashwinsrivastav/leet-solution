1class Solution:
2    def defangIPaddr(self, address: str) -> str:
3        res=""
4        for i in address:
5            if i!=".":
6                res+=i
7            else:
8                res+="[.]"
9        return res
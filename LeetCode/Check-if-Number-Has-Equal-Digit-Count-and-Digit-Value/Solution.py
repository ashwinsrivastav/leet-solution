1class Solution:
2    def digitCount(self, num: str) -> bool:
3        count={'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
4        for i in num:
5            count[i]=count[i]+1
6        for i in range(len(num)):
7            if int(num[i])!=count[str(i)]:
8                return False
9        return True
10       
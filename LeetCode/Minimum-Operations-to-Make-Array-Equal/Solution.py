1class Solution:
2    def minOperations(self, n: int) -> int:
3        arr=[];op=0
4        for i in range(n):
5            arr.append((2 * i) + 1)
6        target=sum(arr)//n
7        print(target)
8        for i in arr:
9            if i<target:
10                op+=target-i
11            else:
12                return op
13
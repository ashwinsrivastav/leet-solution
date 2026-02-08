1class Solution:
2    def replaceElements(self, arr: List[int]) -> List[int]:
3        maxx=max(arr)
4        for i in range(len(arr)-1):
5            if arr[i]<maxx:
6                arr[i]=maxx
7                continue
8            else:
9                maxx=max(arr[i+1:])
10                arr[i]=maxx
11        arr[-1]=-1
12        return arr
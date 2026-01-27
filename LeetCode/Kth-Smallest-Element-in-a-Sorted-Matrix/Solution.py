 class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lis=sum(matrix,[])
        lis.sort()
        return lis[k-1]

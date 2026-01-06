1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        a=[str(i) for i in nums ]
4        a="".join(a)
5        a=a.split('0')
6        return len(max(a))
7        
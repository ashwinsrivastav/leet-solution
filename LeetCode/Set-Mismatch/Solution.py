1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        sumnn=(len(nums)*(len(nums)+1))//2
4        missing= sumnn-sum(set(nums))
5        return [sum(nums)-sum(set(nums)),missing]
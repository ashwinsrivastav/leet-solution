1class Solution:
2    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
3        nums=list(set(nums1))+list(set(nums2))+list(set(nums3))
4        x=set(nums);res=[]
5        for i in x:
6            if nums.count(i)>1:
7                res.append(i)
8        return res
9        
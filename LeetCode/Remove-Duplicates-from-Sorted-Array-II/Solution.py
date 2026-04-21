class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq={};res=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in freq.keys():
            if freq[i]>2:
                res.extend([i]*2)
            else:
                res.extend([i]*freq[i])
        nums[:]=res

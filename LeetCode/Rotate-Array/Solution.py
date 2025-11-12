class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k<len(nums):
            counter=1;new=[];i=0
            while counter<=k:
                new.append(nums[-counter])
                counter+=1
            new=new[::-1]
            for i in range(len(nums)-k):
                new.append(nums[i])
            nums[:]=new
        else:
            counter=0;new=[];i=0
            while counter<k:
                new.append(nums[-1])
                nums.remove(nums[-1])
                new.extend(nums)
                nums[:]=new
                new=[]
                counter+=1
            

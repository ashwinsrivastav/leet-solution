class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        count=0;index=0;lim=len(nums)-2
        while nums[index]<nums[index+1]:
            count=1
            if index<lim:
                index+=1
            else:
                return False
        if count==1:
            if nums[index]>nums[index+1]:
                while nums[index]>nums[index+1]:
                    count=2
                    if index<lim:
                        index+=1
                    else:
                        return False
            else:
                return False
        else:
            return False
        if count==2:
            if nums[index]<nums[index+1]:
                while nums[index]<nums[index+1]:
                    count=3
                    if index<lim:
                        index+=1
                    else:
                        break
                if nums[index]<nums[index+1]:
                    pass
                else:
                    return False
            else:
                return False
        else:
            return False
        return True

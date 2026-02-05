def nextindex(n,lenght):
    if n>=0:
        return n%lenght
    else:
        return n+lenght
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        lenght=len(nums);res=[]
        for i in range(lenght):
            n=nums[i]
            if n!=0:
                newindex=nextindex(i+n,lenght)
                while abs(newindex)>lenght:
                    newindex=nextindex(newindex,lenght)
                res.append(nums[newindex])
            else:
                res.append(nums[i])
        return res

    
    

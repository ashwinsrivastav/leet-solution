1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        ans=[]
4        for i,j in zip(range(n),range(n,2*n)):
5            ans.append(nums[i])
6            ans.append(nums[j])
7        return ans
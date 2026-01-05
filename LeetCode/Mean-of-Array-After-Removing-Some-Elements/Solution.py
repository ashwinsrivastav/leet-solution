class Solution:
    def trimMean(self, arr: List[int]) -> float:
        remove=len(arr)//20;arr=sorted(arr)
        arr=arr[remove:-remove]
        return sum(arr)/len(arr)
            

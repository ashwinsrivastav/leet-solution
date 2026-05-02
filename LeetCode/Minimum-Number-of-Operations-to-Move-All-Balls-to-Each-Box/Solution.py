class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        position=[] #will come back after learning prefix sum!!!!
        for i in range(len(boxes)):
            if boxes[i]=="1":
                position.append(i)
        res=[]
        for i in range(len(boxes)):
            sum=0
            for j in position:
                sum+=abs(i-j)
            res.append(sum)
        return res

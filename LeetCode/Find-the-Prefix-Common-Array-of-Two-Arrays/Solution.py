class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen=set();c=[];count=0
        for i in range(len(A)):
            seen.add(A[i])
            for j in range(i+1):
                if B[j] in seen:
                    count+=1
            c.append(count)
            count=0
        return c

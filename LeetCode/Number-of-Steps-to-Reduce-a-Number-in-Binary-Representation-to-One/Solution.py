class Solution:
    def numSteps(self, s: str) -> int:
        p=int(s,2);steps=0
        while p!=1:
            if p%2==0:
                p=p//2
            else:
                p+=1
            steps+=1
        return steps
            

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1="";stack2=""
        for i in s:
            if i!="#":
                stack1+=i
            else:
                stack1=stack1[:-1]
        for i in t:
            if i!="#":
                stack2+=i
            else:
                stack2=stack2[:-1]
        return stack1==stack2

1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack=[];expres=['+', '-', '*','/']
4        for i in tokens:
5            if i not in expres:
6                stack.append(int(i))
7            else:
8                a=stack.pop()
9                b=stack.pop()
10                if i=='+':
11                    stack.append(a+b)
12                elif i=='*':
13                    stack.append(a*b)
14                elif i=='/':
15                    if b//a>=0:
16                        stack.append(b//a)
17                    else:
18                        stack.append(-(-b//a))
19                else:
20                    stack.append(b-a)
21        return stack[0]
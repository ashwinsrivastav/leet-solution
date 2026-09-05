1class Solution:
2    def asteroidCollision(self, asteroids):
3        def repeater(asteroids):
4            stack=[0]
5            stack.append(asteroids[0])
6            top=1
7            for i in range(1,len(asteroids)):
8                if asteroids[i]<0:
9                    if stack[top]>0:
10                        if abs(asteroids[i])>stack[top]:
11                            stack.pop()
12                            stack.append(asteroids[i])
13                        elif abs(asteroids[i])==stack[top]:
14                            stack.pop()
15                            top-=1
16                        else:
17                            pass
18                    else:
19                        stack.append(asteroids[i])
20                        top+=1
21                else:
22                    stack.append(asteroids[i])
23                    top+=1
24            return stack[1:]
25        temp=asteroids
26        temp2=repeater(temp)
27        while temp!=temp2:
28            if temp2==[]:
29                return []
30            temp=temp2
31            temp2=repeater(temp)
32        return temp
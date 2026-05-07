1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        n=len(rooms)-1
4        n=(n*(n+1))//2
5        i=0
6        visited=rooms[0]
7        while i<len(visited):
8            for j in rooms[visited[i]]:
9                if j not in set(visited):
10                    visited.append(j)
11            i+=1
12        if sum(visited)==n:
13            return True
14        return False
15
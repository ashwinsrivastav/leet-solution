1class Solution:
2    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
3        time=0
4        for i in range(len(timeSeries)):
5            if i==0:
6                time=duration
7            else:
8                if timeSeries[i-1]+duration<=timeSeries[i]:
9                    time+=duration
10                elif timeSeries[i-1]+duration>timeSeries[i]:
11                    time+= timeSeries[i]-timeSeries[i-1]
12        return time
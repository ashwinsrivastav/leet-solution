1class Solution:
2    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
3        hap=0;players.sort();trainers.sort();count=0
4        for i in trainers:
5            if i>=players[count]:
6                hap+=1
7                if count<len(players)-1:
8                    count+=1
9                else:
10                    return hap
11        return hap
12       
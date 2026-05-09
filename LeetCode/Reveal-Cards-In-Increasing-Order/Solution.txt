1class Solution:
2    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
3        deck.sort(reverse=True)
4        res=[deck[0]];deck.pop(0)
5        for i in range(len(deck)):
6            temp=res[0]
7            res.pop(0)
8            res.append(temp)
9            res.append(deck[i]) 
10        res.reverse()
11        return res
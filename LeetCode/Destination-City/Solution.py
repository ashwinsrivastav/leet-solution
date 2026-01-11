1class Solution:
2    def destCity(self, paths: List[List[str]]) -> str:
3        outgoing=set([i[0] for i in paths])
4        res=[i[1] for i in paths if i[1] not in outgoing ]
5        return res[0]
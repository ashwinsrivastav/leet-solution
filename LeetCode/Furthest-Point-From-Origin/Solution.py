class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        countl=moves.count("L")
        countr=moves.count("R")
        count_=moves.count("_")
        if countl>countr:
            return countl+count_-countr
        return countr+count_-countl

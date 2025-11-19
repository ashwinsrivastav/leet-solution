class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        try:
            while len(bits)>1:
                if bits[0]==1:
                    bits.pop(0)
                    bits.pop(0)
                else:
                    bits.pop(0)
            if bits[0]==0:
                return True
            else: return False
        except:
            return False
        return True

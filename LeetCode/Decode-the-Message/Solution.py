class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        decoder={" ":" "}
        key="".join((key.split(" ")));visited="";c=0
        for i in key:
            if i not in visited:
                decoder[i]=alpha[c]
                c+=1
                visited+=i
            if c>26:
                break
        res=""
        for i in message:
            res+=decoder[i] 
        return res

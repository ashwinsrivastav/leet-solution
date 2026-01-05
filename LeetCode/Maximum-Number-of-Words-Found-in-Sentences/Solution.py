class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        space=0;max=0
        for i in sentences:
            space=i.count(" ")
            if space>max:
                max=space
        return max+1

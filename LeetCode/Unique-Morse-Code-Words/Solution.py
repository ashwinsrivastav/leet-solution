class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        sett=set();word=""
        for i in words:
            for j in i:
                word+=dic[j]
            if word not in sett:
                sett.add(word)
            word=""
        return len(sett)

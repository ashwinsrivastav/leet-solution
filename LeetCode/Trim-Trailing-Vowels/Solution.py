class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowel={'a', 'e', 'i', 'o', 'u'};d=""
        for i in s[::-1]:
            if i in vowel:
                d=i+d
            else:
                break
        return s.rstrip(d)

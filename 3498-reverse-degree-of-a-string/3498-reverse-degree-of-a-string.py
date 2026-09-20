class Solution:
    def reverseDegree(self, s: str) -> int:
        c = 0
        a = 0
        for i in range(len(s)):
            a = 27 - (ord(s[i].upper()) - 64)
            a = a * (i + 1)
            c += a
            a = 0
        return c


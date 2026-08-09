class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = []
        l = s.split()
        a = l[-1]
        return len(a) 
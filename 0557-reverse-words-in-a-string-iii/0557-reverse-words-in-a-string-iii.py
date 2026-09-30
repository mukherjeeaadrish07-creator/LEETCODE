class Solution:
    def reverseWords(self, s: str) -> str:
        sentence =""
        a = 0
        b = []
        a = s.split()
        for i in a:
            b.append(i[::-1])
        
        sentence = " ".join(b)
        return sentence


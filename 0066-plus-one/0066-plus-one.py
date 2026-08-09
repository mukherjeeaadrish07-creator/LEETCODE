class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        C = 0
        l = []
        for i in digits:
            C = str(C) + str(i)
        a = int(C) + 1
        for i in str(a):
            l.append(int(i))
            
        return l

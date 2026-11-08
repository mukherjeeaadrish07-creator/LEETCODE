class Solution:
    def countDigits(self, num: int) -> int:
        C = 0
        n = num
        temp = 0
        while num > 0:
            temp = num % 10
            num = num // 10
            if temp != 0 and n % temp == 0:
                C += 1
        return C

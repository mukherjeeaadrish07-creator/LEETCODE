class Solution:
    def countCommas(self, n: int) -> int:
        C = 0
        if n < 1000:
            return 0
        else:
            for i in range(3,16,3):
                if n >= 10**i:
                    C = C + n - 10**i + 1
            return C
                        
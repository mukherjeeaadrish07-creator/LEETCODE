class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = list(str(n))
        C = 0
        P = 1
        for i in a:
            C = C + int(i)

        for j in a:
            P = P* int(j)

        if n % (C + P) == 0:
            return True
        else:
            return False

        
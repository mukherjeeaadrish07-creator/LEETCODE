class Solution:
    def digitSum(self, s: str, k: int) -> str:
        i = 0
        C = 0
        while len(s) > k:
            new_str = ""
            for i in range(0, len(s), k):
                group = s[i:i+k]
                for j in group:
                    C += int(j)
                new_str += (str(C))
                C = 0
            s = new_str
        return str(s)
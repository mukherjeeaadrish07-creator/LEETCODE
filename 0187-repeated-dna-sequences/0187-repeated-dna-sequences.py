class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a = []
        ans = []
        count = {}

        for i in range(len(s) - 9):
            window = s[i:i+10]
            a.append(window)

        for j in a:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1

        for j in a:
            if count[j] > 1 and j not in ans:
                ans.append(j)

        return ans

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        lst = []
        l1 = []
        a = 0

        for i in range(1, len(nums) + 2):
            a = k * i
            lst.append(a)

        lst.sort()

        for j in lst:
            if j not in nums:
                return j
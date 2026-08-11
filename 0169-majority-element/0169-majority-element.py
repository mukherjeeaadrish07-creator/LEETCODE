class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        v = 0
        for i in nums:
            if v == 0:
                c = i

            if i == c:
                v += 1
            else:
                v -= 1

        return c
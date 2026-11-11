class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        e_sum = 0
        d_sum = 0
        for i in nums:
            e_sum += i

        for i in nums:
            for j in str(i):
                d_sum += int(j)
        return e_sum - d_sum
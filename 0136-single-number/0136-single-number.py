class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        C = 0
        for i in range(len(nums)):
            C = C ^ nums[i]
        return C
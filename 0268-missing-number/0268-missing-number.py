class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        m = nums[0] 
        for i in nums:
            if i > m:
                m = i

        for i in range(0,m+1):
            if i not in nums:
                return i

        return m+1

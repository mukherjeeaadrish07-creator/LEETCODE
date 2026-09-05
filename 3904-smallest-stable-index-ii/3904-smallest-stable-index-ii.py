class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if not nums:
            return -1
        
        n = len(nums)
        mi = [0] * n
        mi[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            mi[i] = min(nums[i],mi[i+1])

        ma = nums[0]
        for i in range(n):
            ma =  max(ma, nums[i])

            if ma - mi[i] <= k:
                return i
        return -1
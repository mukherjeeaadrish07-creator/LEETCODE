class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l1 = []
        l2 = []
        a = 0
        b = 0
        for i in range(0,len(nums)):
            a = max(nums[0:i+1])
            b = min(nums[i:len(nums)])

            if a - b <= k:
                    return i
        return -1

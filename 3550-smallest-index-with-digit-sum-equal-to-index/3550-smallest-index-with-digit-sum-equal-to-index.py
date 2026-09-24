class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        
        for i in range(len(nums)):
            C = 0
            a = nums[i]
            while (a>0):
                C = C + a %10
                a = a//10
            if C == i:
                return i
        return -1

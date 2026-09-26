class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                return True
            else:
                i += 1
                j += 1
        return False
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)+1):
            if nums[i] == target:
                return i
            #elif target == 0:
                #return 0
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)
        return nums
                
                        
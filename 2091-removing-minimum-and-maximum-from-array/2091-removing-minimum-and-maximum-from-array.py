class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Make min_index the smaller index
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        # Both from the left
        left = max_index + 1

        # Both from the right
        right = n - min_index

        # One from left, one from right
        both = (min_index + 1) + (n - max_index)

        return min(left, right, both)


            
        
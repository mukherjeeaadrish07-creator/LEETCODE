class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        a =0
        b = 0
        arr = []
        while len(nums) != 0:
            a = min(nums)
            nums.remove(a)
            b = min(nums)
            nums.remove(b)

            arr.append(b)
            arr.append(a)

        return arr

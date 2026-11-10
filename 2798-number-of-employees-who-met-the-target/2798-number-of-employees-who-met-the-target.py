class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        C = 0
        for i in hours:
            if i >= target:
                C += 1
        return C
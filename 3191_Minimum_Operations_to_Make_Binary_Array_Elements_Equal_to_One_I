class Solution:
    def minOperations(self, nums: List[int]) -> int:
        opp = 0
        for i,n in enumerate(nums):
            if n == 0:
                if i+2 >= len(nums):
                    return -1
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                opp += 1
        return opp

#General idea: turn the leftmost 0 to 1, keeping track of operations. If it gets out of the array, return -1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        limit = len(nums)
        new_target = limit
        for i,item in enumerate(nums[::-1]):
            jump = item
            if (limit - i) + jump >= new_target:
                new_target = limit - i
        if new_target == 1:
            return True
        return False
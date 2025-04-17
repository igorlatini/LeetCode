class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = {}
        for item in nums:
            if item in cnt:
                del cnt[item]
            else:
                cnt[item] = 1
        return cnt == {}

#General idea: use a dict to keep track

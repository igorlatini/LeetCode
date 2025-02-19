class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_list = []
        for i,number in enumerate(nums):
            if target - number in sum_list:
                return [sum_list.index(target-number), i]
            else:
                sum_list.append(number)

#General idea: keep track of the target values, checking for them for each item

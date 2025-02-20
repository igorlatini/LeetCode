class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        for i in range(pow(2, len(nums))):
            if i >= len(nums) or i != int(nums[i], 2):
                number_string = str(bin(i))[2:]
                return  '0'*(len(nums) - len(number_string)) + number_string

#General idea: check if the number in binary is the same as its position and, if not, return it in string form 
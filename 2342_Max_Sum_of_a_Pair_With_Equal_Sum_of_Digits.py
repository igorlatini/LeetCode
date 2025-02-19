class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_digits = {}
        best_value = -1
        for i,item in enumerate(nums):
            value = self.get_digits(item)
            if value not in sum_digits:
                sum_digits[value] = item
            else:
                if sum_digits[value] + item > best_value:
                    best_value = sum_digits[value] + item
                if item > sum_digits[value]:
                        sum_digits[value] = item                        
        return best_value


    def get_digits(self, item):
        sum_total = 0
        for i in str(item):
            sum_total += int(i)
        return sum_total

#General idea: directly keep track of the best sum and the highest sum of digits

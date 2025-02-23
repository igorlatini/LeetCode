class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carrier = 1
        for i, value in enumerate(digits):
            digits[-(i+1)] += carrier
            if digits[-(i+1)] >= 10:
                digits[-(i+1)] -= 10
                carrier = 1
            else:
                carrier = 0
                break
        if carrier:
            digits = [1] + digits
        return digits

#General idea: array in reverse order, keeping track of the carrier
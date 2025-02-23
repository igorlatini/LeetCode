class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

#General idea: transform the number into a binary string and count the 1s
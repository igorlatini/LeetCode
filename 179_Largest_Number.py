class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=self.normalizeSize, reverse=True)
        result = ''
        for i in nums:
            result += str(i)
        return str(int(result))

    def normalizeSize(self, e):
        e = str(e)
        while(len(e) < 10):
            e += str(e)
        return e

#General idea: sort the string, repeat each string to have at least 10 chars (max size of an input)

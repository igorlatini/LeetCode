class Solution:
    def reverse(self, x: int) -> int:
        negative = 0
        limit = '2147483647'
        if x < 0:
            negative = True
            x -= 2*x
            limit = '2147483648'
        string = str(x)
        reversed_string = string[::-1]
        if len(reversed_string) == len(limit):
            for i, letter in enumerate(reversed_string):
                if int(letter) > int(limit[i]):
                    return 0
                elif int(letter) < int(limit[i]):
                    break
        if negative:
            return int('-' + reversed_string)
        return int(reversed_string)
    
#General idea: read the number as string, keep the signal elsewhere, check for limits with each char
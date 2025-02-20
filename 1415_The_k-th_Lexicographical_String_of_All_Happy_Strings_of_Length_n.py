class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        size_of_possible = 3 *(pow(2, n-1))
        if k > size_of_possible:
            return ''
        result = self.get_next('', size_of_possible, k)
        return result
        
    def get_next(self, last, size_p, k):
        if last == '':
            new_size = size_p/3
            new_k = k%new_size
            if new_k == 0:
                new_k = new_size 
            if k <= new_size:
                new_letter = 'a'
            elif k <= 2*new_size:
                new_letter = 'b'
            else:
                new_letter = 'c'
            return new_letter + self.get_next(new_letter, new_size, new_k)
        if size_p == 1:
            return ''
        new_size = size_p/2
        new_k = k%new_size
        if new_k == 0:
            new_k = new_size
        if last == 'a':
            if k <= new_size:
                new_letter = 'b'
            else:
                new_letter = 'c'
        elif last == 'b':
            if k <= new_size:
                new_letter = 'a'
            else:
                new_letter = 'c'
        else:
            if k <= new_size:
                new_letter = 'a'
            else:
                new_letter = 'b'
        return new_letter + self.get_next(new_letter, new_size, new_k)
    
#General idea: you can divide the list of strings initially by 3, and then by two each time, adjusting k 
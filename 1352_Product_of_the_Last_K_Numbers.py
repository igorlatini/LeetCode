class ProductOfNumbers:

    def __init__(self):
        self.number_list = []

    def add(self, num: int) -> None:
        if len(self.number_list) == 0:
            self.number_list.append(num)
        if num == 0:
            self.number_list = []
        else:
            self.number_list.append(num*self.number_list[-1])

    def getProduct(self, k: int) -> int:
        if len(self.number_list) == 0:
            return 0
        if k+1 > len(self.number_list) or self.number_list[-(k+1)] == 0:
            return 0
        return int(self.number_list[-1]/self.number_list[-(k+1)])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

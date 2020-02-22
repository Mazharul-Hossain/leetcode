class ProductOfNumbers:

    def __init__(self):
        self.product = []
        self.pointer = 0
        

    def add(self, num: int) -> None:
        if num == 0 :
            for i in range(self.pointer, len(self.product)):
                self.product[i] = num
            self.pointer = len(self.product)
        if num > 1 :
            for i in range(self.pointer, len(self.product)):
                self.product[i] *= num 
        self.product.append(num)


    def getProduct(self, k: int) -> int:
        return self.product[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
obj.add(3)        # [3]
obj.add(0)        # [3,0]
obj.add(2)        # [3,0,2]
obj.add(5)        # [3,0,2,5]
obj.add(4)        # [3,0,2,5,4]
print(obj.getProduct(2)) # return 20. The product of the last 2 numbers is 5 * 4 = 20
print(obj.getProduct(3)) # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
print(obj.getProduct(4)) # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
obj.add(8)               # [3,0,2,5,4,8]
print(obj.getProduct(2)) # return 32. The product of the last 2 numbers is 4 * 8 = 32 
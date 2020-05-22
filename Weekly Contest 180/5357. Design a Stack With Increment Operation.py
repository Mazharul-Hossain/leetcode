class CustomStack:

    def __init__(self, maxSize: int):
        self.stack_list = [0 for i in range(maxSize)]
        self.maxSize = maxSize
        self.pointer = 0

    def push(self, x: int) -> None:
        if self.pointer < self.maxSize: 
            self.stack_list[ self.pointer ] = x
            self.pointer += 1
        # print(self.pointer, self.stack_list)
        

    def pop(self) -> int:
        if self.pointer > 0:
            self.pointer -= 1
            return self.stack_list[ self.pointer]
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < k and i < self.pointer:
            self.stack_list[ i ] += val
            i += 1
        


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
print( obj.pop() ) 
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5,100)
obj.increment(2,100)
print( obj.pop() )
print( obj.pop() )
print( obj.pop() )
print( obj.pop() )
class MinStack:
    def __init__(self):
        self.stack={}
        self.pointer=-1
        self.values={}

    def push(self, val: int) -> None:
        self.pointer+=1
        self.stack[self.pointer]=val

        if self.pointer == 0:
            self.values[self.pointer] = val
        else:
            if val < self.values[self.pointer-1]: self.values[self.pointer] = val
            else: self.values[self.pointer] = self.values[self.pointer - 1]
            

    def pop(self) -> None:
        self.pointer-=1

    def top(self) -> int:
        return self.stack[self.pointer]

    def getMin(self) -> int:
        return self.values[self.pointer]
        

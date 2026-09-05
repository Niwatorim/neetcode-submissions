class Solution:
    def isValid(self, s: str) -> bool:
        stack =[None for i in s]
        opened = ["(","{","["]
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }
        pointer = -1
        for i in s:
            if i in opened:
                pointer+=1
                stack[pointer]=i
            else:
                if pointer != -1:
                    if pairs[i] == stack[pointer]:
                        pointer -=1
                    else:
                        return False
                else:
                    return False
        if pointer != -1:
            return False
        return True

"""
stack -> if open then add to stack
if closed then pop from stack
"""
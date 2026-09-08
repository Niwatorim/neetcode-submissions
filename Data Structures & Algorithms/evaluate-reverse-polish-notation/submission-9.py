
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Make stack
        if an item comes, its the top two items in stack that get the thing done to it
        """
        stack = []
        operators={"+","-","*","/"}
        deletions=0
        for i in range(len(tokens)):
            if tokens[i] in operators:
                stack_i=i-deletions
                num1 = stack[stack_i-1]
                num2 = stack[stack_i-2]
                match tokens[i]:
                    case "+": 
                        stack[stack_i-2] = num1 + num2 
                        del stack[stack_i-1]
                        deletions+=2
                    case "-": 
                        stack[stack_i-2] = num2 - num1
                        del stack[stack_i-1]
                        deletions+=2
                    case "/":
                        stack[stack_i-2] = int(num2 / num1)
                        del stack[stack_i-1]
                        deletions+=2
                    case "*":
                        stack[stack_i-2] = num1 * num2 
                        del stack[stack_i-1]
                        deletions+=2
                        
            else:
                stack.append(int(tokens[i]))
            
        return stack[0]

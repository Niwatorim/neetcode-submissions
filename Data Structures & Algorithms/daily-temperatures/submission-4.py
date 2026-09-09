class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output=[0 for j in range(len(temperatures))]
        for i, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                idx = stack.pop()
                output[idx] = i - idx
            stack.append(i)
        return output
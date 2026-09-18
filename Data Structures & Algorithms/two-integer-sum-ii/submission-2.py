class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while True:
            summed = numbers[left]+numbers[right]
            if summed > target:
                right-=1
            elif summed < target:
                left+=1
            else:
                return [left+1,right+1]

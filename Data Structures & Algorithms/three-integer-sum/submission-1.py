class Solution:
    def twoSum(self,nums: List[int],target: int):
        left= 0
        right=len(nums)-1
        pairs=[]
        while left<right:
            summed = nums[left] + nums[right]
            if (summed) == target:
                pairs.append([nums[left], nums[right]])
                left+=1
                right-=1
            elif summed > target:
                right-=1
            elif summed < target:
                left+=1
        return pairs
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers= set()
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            valid_array = nums[:] #pop the value from the array
            valid_array.pop(i)

            all_pairs = self.twoSum(valid_array,-nums[i])
            
            for pair in all_pairs:
                    triplet = tuple(sorted([nums[i], pair[0], pair[1]]))
                    answers.add(triplet)

        return [list(t) for t in answers]


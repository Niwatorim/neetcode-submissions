class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Anything in the set, make it point to the next number if its in the array
        else point to none.
        Then hop between things and see the biggest hop
        """
        numbers = set(nums)
        longest = 0
        for i in numbers:
            if i-1 not in numbers:
                current_number = i
                current_streak = 1
                while current_number+1 in numbers:
                    current_streak+=1
                    current_number +=1

                longest= max(longest,current_streak)
        return longest



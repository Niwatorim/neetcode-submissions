class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        flag = nums.count(0)
        # 3 situations:
        # no 0
        # 1 zero
        # 3 zeros
        if flag == 0:
            total = 1
            for i in nums:
                total*=i
            for i in nums:
                final.append(int(total/i))
        if flag == 1:
            total = 1
            for i in nums:
                if i!=0:
                    total*=i
            for i in nums:
                if i != 0: final.append(0)
                else: final.append(total)
        if flag >= 2:
            for i in nums:
                final.append(0)
        return final
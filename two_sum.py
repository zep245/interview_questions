from typing import List


class Solution:
    def two_sum(self , nums : List[int] , target: int):
        for i in range(0 ,len(nums)+1):
            for j in range(i+1 , len(nums)+1):
                if nums[i] + nums[j] == target:
                    return [i , j]
                


s = Solution()

print(s.two_sum([2,7,11,15] , 9))
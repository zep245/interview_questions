from typing import List


class Solution:
    def missing_number(self ,nums: List[int]):
        n = len(nums)
        total_sum = n *(n+1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum
    

s = Solution()
print(s.missing_number([3,0,1]))
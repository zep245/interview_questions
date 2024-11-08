from typing import List


class Solution:
    def dissapper_nums(self , nums: List[int]):
        n = max(nums)
        full_set = set(range(1 , n+1))
        actual_set = set(nums)
        missing_nums = list(full_set - actual_set)
        return missing_nums
    


s = Solution()
print(s.dissapper_nums([3, 5, 6, 1, 7]))
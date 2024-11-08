#[1,1,2,2,3,4,4,5,5]      o/p == [3]


from typing import List

class solution:
    def not_repeact(self , nums : List[int]):
        for i in range(0 , len(nums)+1):
            for j in range(i+1 , len(nums)+1):
                if nums[i] == nums[j]:
                    
                
s = solution()

print(s.not_repeact([1,1,2,2,3,4,4,5,5]))
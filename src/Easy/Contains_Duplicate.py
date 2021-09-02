from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    



if __name__ == "__main__":
    assert(Solution().containsDuplicate([1,2,3,4,1]) == True) # Duplicate
    assert(Solution().containsDuplicate([1,2,3,4]) == False) # No Duplicate
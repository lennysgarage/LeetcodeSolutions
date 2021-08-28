from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while (i < len(nums)):
            j = nums[i] - 1 # 3 - 1 => index 2
            if nums[i] != nums[j]: # if value doesn't equal it's sorted index
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        missing_nums = []
        for x in range(0, len(nums)):
            if nums[x] != x+1:
                missing_nums.append(x+1)
        return missing_nums
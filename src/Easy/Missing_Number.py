from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(0, n):
            total += nums[i]
        return (n * (n+1) //2) - total; # n*(n+1)//2 sum of n numbers
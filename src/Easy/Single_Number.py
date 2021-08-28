from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single = single ^ num # 0 XOR ?? = ?? && ?? XOR ?? = 0
        return single
    
    
    # TLDR; duplicates cancel each other out due to XOR operation 
    # Leaving only the single value left
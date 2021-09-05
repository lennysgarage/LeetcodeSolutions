from typing import List

class Solution:
    def determine_unique(self, s: str):
        d = {}
        for char in s:
            if char in d:
                return False # Contains a duplicate
            else:
                d[char] = char
        return True
    
    def determine_unique_set(self, s: str):
        return len(set(s)) == len(s)



if __name__ == "__main__":
    assert(Solution().determine_unique('abcdefg') == True)
    assert(Solution().determine_unique_set('abcdefg') == True)
    assert(Solution().determine_unique('abcdefaghi') == False)
    assert(Solution().determine_unique_set('abcdefaghi') == False)
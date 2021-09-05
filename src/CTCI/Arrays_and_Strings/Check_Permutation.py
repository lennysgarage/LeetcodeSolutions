from typing import List

class Solution:
    def determine_permutation(self, s1: str, s2: str):
        if len(s1) != len(s2): # Permutation requires the strings to have the same length
            return False

        letters = {} # If we know size of character set like ASCII we could make a list of [None] * size
        # Get frequency of each character in first string
        for char in s1:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        
        # Check if every character in second string is also a character in first
        for char in s2:
            if char not in letters:
                return False
            letters[char] -= 1
            if letters[char] < 0:
                return False # We need more letters than available
        return True
            

if __name__ == "__main__":
    assert(Solution().determine_permutation('abcae', 'fbcaa') == False)
    assert(Solution().determine_permutation('aabc', 'abac') == True)
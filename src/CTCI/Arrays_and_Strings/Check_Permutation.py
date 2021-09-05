import unittest
from collections import Counter


class Solution:
    def determine_permutation(self, s1: str, s2: str):
        if len(s1) != len(s2):  # Permutation requires the strings to have the same length
            return False

        letters = {}  # If we know size of character set like ASCII we could make a list of [None] * size
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
                return False  # We need more letters than available
        return True

    def determine_permutation_pythonic(self, s1: str, s2: str):
        if len(s1) != len(s2):
            return False

        return Counter(s1) == Counter(s2)


class Test(unittest.TestCase):
    test_cases = [
        ("abcae", "fbcaa", False),
        ("aabc", "abac", True),
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    ]
    test_functions = [
        Solution().determine_permutation,
        Solution().determine_permutation_pythonic,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.test_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()

from typing import List


class ArrayAndHashing:

    def scoreOfString(self, s: str) -> int:
        """
        1. Score of a String

        You are given a string `s`. The score of a string
        is defined as the sum of the absolute difference between ASCII
        value of adjacent character.

        Return the score of `s`.
        """

        sum = 0
        for i in range(len(s) - 1):
            sum = sum + abs(ord(s[i]) - ord(s[i+1]))

        return sum

    def hasDublicate(self, nums: List[int]) -> bool:
        """
        2. Contains Duplicate

        Given an integer array `nums`, return `true`
        if any value appears more than once in the array,
        otherwise return `false`
        """

        return len(set(nums)) != len(nums)

    def isAnagram(self, s: str, t: str) -> bool:
        """
        3. Valid Anagram

        Given two string `s` and `t`, return `true` if the two strings
        are anagrams of each other, otherwise return `false`

        An `anagram` is a string that contains the exact same characters
        as another string, but the order of the characters can be different.
        """
        if len(s) != len(t):
            return False

        charFreqS, charFreqT = {}, {}

        for i in range(len(s)):
            charFreqS[s[i]] = 1 + charFreqS.get(s[i], 0)
            charFreqT[t[i]] = 1 + charFreqT.get(t[i], 0)

        return charFreqS == charFreqT

    def replaceElement(self, arr: List[int]) -> List[int]:
        """
        4. Replace Element With Greatest Element On Right Side

        You are given an array `arr`, replace every element in that array with
        the greatest element among the element to its right,
        and replace the last element with `-1`.

        After doing so, return the array.
        """

        # length = len(arr)
        #
        # for i in range(length):
        #
        #     if i == length - 1:
        #         arr[i] = -1
        #
        #     else:
        #         arr[i] = max(arr[(i + 1): length])
        #

        maxVal = -1

        for i in range(len(arr) - 1, -1, -1):

            currentVal = arr[i]

            arr[i] = maxVal

            if currentVal > maxVal:
                maxVal = currentVal

        return arr

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        5. Is Subsequence

        You are given the strings `s` and `t`.
        Return `true` if s is a `subsequence` of `t`, or `false` otherwise

        A `subsequence` of a string is a new string that is formed from the
        original string by deleting some (can be none) of the characters
        without distrubing the relative positions of the remaining characters.
        (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not)
        """

        sIndex = tIndex = 0

        while sIndex < len(s) and tIndex < len(t):
            if s[sIndex] == t[tIndex]:
                sIndex += 1

            tIndex += 1

        return sIndex == len(s)

    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        6. Concatenation of Array

        You are given an interger array `nums` of length `n`. Create ans
        array `ans` of length `2n` where `ans[i] == nums[i]` and
        `ans[i+n] == nums[i]` for `0<= i < n` (0-indexed)
        """

        nums.extend(nums)

        return nums

    def appendCharacters(self, s: str, t: str) -> int:
        """
        7. Append Characters to String to Make Subsequence

        You are given the strings `s` and `t` consisting of only lowercase
        English letters.

        return the minimum number of characters that need to be appended to the
        end of `s` so that `t` becomes a subsequence of `s`.

        A `subsequence` of a string is a new string that is formed from the
        original string by deleting some (can be none) of the characters
        without distrubing the relative positions of the remaining characters.
        (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not)
        """

        sIndex = tIndex = 0

        while sIndex < len(s) and tIndex < len(t):
            if s[sIndex] == t[tIndex]:
                tIndex += 1

            sIndex += 1

        return len(t) - tIndex

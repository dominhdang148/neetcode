from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    """
    6. Concatenation of Array

    You are given an interger array `nums` of length `n`. Create an array `ans`
    of length `2n` where `ans[i] == nums[i]` and `ans[i+n] == nums[i]`
    for `0<= i < n` (0-indexed)
    """

    nums.extend(nums)

    return nums

from typing import List


def hasDublicate(nums: List[int]) -> bool:
    """
    2. Contains Duplicate

    Given an integer array `nums`, return `true`
    if any value appears more than once in the array,
    otherwise return `false`
    """

    return len(set(nums)) != len(nums)

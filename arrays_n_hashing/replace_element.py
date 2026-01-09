from typing import List


def replaceElement(arr: List[int]) -> List[int]:
    """
    4. Replace Element With Greatest Element On Right Side

    You are given an array `arr`, replace every element in that array with the
    greatest element among the element to its right,
    and replace the last elemnt with `-1`.

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

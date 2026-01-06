def scoreOfString(s: str) -> int:
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

def isSubsequence(s: str, t: str) -> bool:
    """
    5. Is Subsequence

    You are given the strings `s` and `t`.
    Return `true` if s is a `subsequence` of `t`, or `false` otherwise

    A `subsequence` of a string is a new string that is formed from the
    original string by deleting some (can be none) of the characters without
    distrubing the relative positions of the remaining characters.
    (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not)
    """

    tIndex = 0
    sIndex = 0

    # print(range(len(s) - 1))

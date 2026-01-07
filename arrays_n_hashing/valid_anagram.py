def isAnagram(s: str, t: str) -> bool:
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

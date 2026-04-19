def lengthOfLongestSubstring(s: str) -> int:
    """
    Given a string s, finds the length of the longest substring without duplicate characters.
    """

    s = list(s)
    best = ''
    current = ''

    stack = []

    i = 0

    while i < len(s):
        if s[i] not in current:
            current += s[i]
            stack.append(i)
            i += 1
            if len(current) > len(best):
                best = current
        else:
            i = stack[0] + 1
            current = '' + s[i]
            stack = [i]
            i += 1

    return len(best)


            

print(lengthOfLongestSubstring(s="bbbbbb"))
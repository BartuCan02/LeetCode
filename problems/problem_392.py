def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
            
    start = 0
    i = 0

    while i < len(t):
        if s[start] != t[i]:
            i += 1
        else:
            start += 1
            if start == len(s):
                    return True
            i += 1

    return False

        
print(isSubsequence(s="", t="abc"))



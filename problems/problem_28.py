def strStr(haystack:str, needle:str) -> str:
    if needle not in haystack:
        return -1
    else:
        return haystack.find(needle)
    

print(strStr("abc", "bc"))
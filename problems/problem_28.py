def strStr(haystack:str, needle:str) -> str:
    
    """
    Given two strings needle and haystack,
    return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
    """
    

    if needle not in haystack:
        return -1
    else:
        return haystack.find(needle)
    

def strStr(haystack:str, needle:str) -> str:
    
    """
    The solution with not built in function
    """
    
    if needle not in haystack:
        return -1
   
    for i in range(len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            return i
        
    return -1


print(strStr("sadbutsad", "sad"))
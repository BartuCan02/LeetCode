def gcdOfStrings(str1: str, str2: str) -> str:
        best = ""

        if len(str1) >= len(str2):
            for i in range(len(str2)):
                x = str2[:i+1]
                st1 = len(str1) // len(x)
                st2 = len(str2) // len(x)

                if (str1 == (x * st1) and str2 == (x * st2)):
                     best = x
                else:
                     continue
        else:
            for i in range(len(str1)):
                x = str1[:i+1]
                st1 = len(str1) // len(x)
                st2 = len(str2) // len(x)

                if (str1 == (x * st1) and str2 == (x * st2)):
                     best = x
                else:
                     continue
                   
        return best

print(gcdOfStrings(str1 = "AB", str2 = "ABAB"))


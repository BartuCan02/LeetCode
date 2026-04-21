
def is_palindrome(s:str) -> str:
        str_reversed = s[::-1]
        return s == str_reversed


def longestPalindrome(s: str) -> str:
        combinations = []
    
        for i in range(len(s)):
            for j in range(i, len(s)):
                element = s[i:j + 1]
                if is_palindrome(element):
                    combinations.append(element)
        
        output = ''

        for element in combinations:
            if len(element) > len(output):
                output = element
        
        return output


print(longestPalindrome("a"))           

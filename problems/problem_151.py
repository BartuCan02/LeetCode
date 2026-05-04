def reverseWords(s: str) -> str:
        words = s.strip().split()
        print(words)
        return " ".join(words[::-1])


print(reverseWords("the    sky is blue"))
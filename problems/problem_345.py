def reverseVowels(s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A","E", "I", "O", "I"]
        s_reversed_vowels = [i for i in s if i in vowels][::-1]
        list_s = list(s)

        start = 0
        for i, element in enumerate(list_s):
            if element in vowels:
                list_s[i] = s_reversed_vowels[start]
                start += 1

        
        return "".join(list_s)


print(reverseVowels("Ui"))
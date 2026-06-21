def closeStrings(word1: str, word2: str) -> bool:

    from collections import Counter

    dict_word1 = Counter(word1)
    dict_word2 = Counter(word2)

    key_word1 = set(sorted(dict_word1.keys()))
    key_word2 = set(sorted(dict_word2.keys()))

    value_word1 = sorted(dict_word1.values())
    value_word2 = sorted(dict_word2.values())

    value_match = value_word1 == value_word2
    key_match = key_word1 == key_word2

    return True if value_match and key_match else False



print(closeStrings(word1 = "abc", word2 = "bca"))


def mergeAlternately(word1: str, word2: str) -> str:
        
        merged = ""
        
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            merged += word1[i] + word2[i]

        if len(word1) > len(word2):
            merged += word1[len(word2):]
            return merged

        elif len(word1) < len(word2):
            merged += word2[len(word1):]
            return merged
        else:
            return merged

print(mergeAlternately("abcd","pq"))
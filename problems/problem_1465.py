def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiou")

    current_count = sum(1 for char in s[:k] if char in vowels)
    best = current_count

    for right in range(k, len(s)):
        left = right - k

        if s[left] in vowels:
            current_count -= 1

        if s[right] in vowels:
            current_count += 1

        best = max(best, current_count)

    return best
            
print(maxVowels(s="amc", k=2))
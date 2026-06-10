def uniqueOccurrences(arr: List[int]) -> bool:
        hash_map = {}

        for i in arr:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        values_seen = set()
        for value in hash_map.values():
            if value not in values_seen:
                values_seen.add(value)
            else:
                return False

        return True

print(uniqueOccurrences([1,2]))
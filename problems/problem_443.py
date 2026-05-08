def compress(chars: List[str]) -> int:
        s = []
        
        for i in range(len(chars)):
            if chars[i] == chars[i - 1] and (i != 0):
                continue

            count = 0
            for j in range(i,len(chars)):
                if chars[i] == chars[j]:
                    count += 1
                else:
                    break

            if count == 1:
                s.append(chars[i])

            else:
                s.append(chars[i])
                count_str = str(count)
                for num in count_str:
                    s.append(num)     
        
        chars[::] = s

        print(chars)
        return len(s)

print(compress(["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]))





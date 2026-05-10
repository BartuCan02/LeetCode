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
            
            elif 100 > count >= 10:
                s.append(chars[i])
                count_str = str(count)
                s.append(count_str[0])
                s.append(count_str[1])
            
            elif 1000 > count >= 100:
                s.append(chars[i])
                count_str = str(count)
                s.append(count_str[0])
                s.append(count_str[1])
                s.append(count_str[2])
            
            elif count >= 1000:
                s.append(chars[i])
                count_str = str(count)
                s.append(count_str[0])
                s.append(count_str[1])
                s.append(count_str[2])
                s.append(count_str[3])

            else:
                s.append(chars[i]) 
                s.append(str(count))     
        
        chars[::] = s

        print(chars)
        return len(s)

print(compress(["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]))





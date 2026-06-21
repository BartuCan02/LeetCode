def removeStars(s: str) -> str:
    stack = []

    for i in s:
        if i == "*":
            stack.pop()
        else:
            stack.append(i)

        print(stack)
    
    return "".join(stack)

print(removeStars(s = "leet**cod*e"))
print(removeStars(s = "erase*****"))
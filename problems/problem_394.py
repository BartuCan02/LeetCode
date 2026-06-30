
def decodeString(s: str) -> str:
    stack = []

    for ch in s:
        if ch != "]":
            stack.append(ch)
        else:
            # Get current string
            current_str = ""
            while stack[-1] != "[":
                current_str = stack.pop() + current_str
            # Take "[" out
            stack.pop()

            # Get number
            current_num = ""
            while stack and stack[-1].isdigit():
                current_num = stack.pop() + current_num

            current_str = int(current_num) * current_str
            stack.append(current_str)
        
    return "".join(stack)
            

print(decodeString(s = "3[a]2[bc]"))
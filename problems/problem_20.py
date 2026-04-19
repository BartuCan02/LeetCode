class Solution(object):
    def isValid(self, s):
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []

        if len (s) == 0:
            return True

        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == d[stack[-1]]:
                stack.pop()  
            else:
                return False              
        if len(stack) > 0:
            return False

        return True
        

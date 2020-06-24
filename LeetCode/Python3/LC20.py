"""
LeetCode Problem - 20
Allan Hieng
"""

def isValid(str):

    if len(str) == 0:
        return True

    stack = []
    for char in str:
        if char == '(':
            stack.append(char)
        elif char == '[':
            stack.append(char)
        elif char == '{':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            leftBracket = stack.pop()
            if leftBracket == '[':
                if char != ']':
                    return False
            if leftBracket == '(':
                if char!= ')':
                    return False
            if leftBracket == '{':
                if char!= '}':
                    return False
    
    if len(stack) != 0:
        return False
    else:
        return True

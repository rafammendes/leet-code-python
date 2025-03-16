import sys

def isValid(s: str) -> bool:
    open = ['(', '[', '{']
    close = [')', ']', '}']
    if s[0] in close or s[-1] in open:
        return False
    
    stack = []
    for i,char in enumerate(s):
        if char in close:
            if not stack:
                return False
            
            close_id = close.index(char)
            if open[close_id] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
              
    return not stack

print(isValid(sys.argv[1]))
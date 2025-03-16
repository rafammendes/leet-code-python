def romanToInt(s: str) -> int:
    symbols = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if s in symbols:
        return symbols[s]
    size = len(s) -1
    value = 0
    i = 0

    while i <= size:
        if i < size and symbols[s[i]] < symbols[s[i+1]]:
            value -= symbols[s[i]]
            value += symbols[s[i+1]]
            i += 2
        else:
            value += symbols[s[i]]
            i += 1
    
    return value
        

print(romanToInt('LVIII'))
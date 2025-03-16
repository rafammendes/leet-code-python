import sys

def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    if (x < 10):
        return True
    
    x_str = str(x)
    half_size = len(x_str) // 2


    first_half = x_str[0:half_size]
    last_half = x_str[-half_size:][::-1]

    return first_half == last_half

print(isPalindrome(int(sys.argv[1])))
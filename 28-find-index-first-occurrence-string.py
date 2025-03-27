def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1


print(strStr("mississippi", "issip"))
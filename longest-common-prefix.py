from typing import List
import sys


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    result = ''
    shortest_word = min(strs, key=len)
    strs.remove(shortest_word)
    for i, char in enumerate(shortest_word):
        if all(word[i] == char for word in strs): 
            result = result + char
        else:
            return result
        
    return result


input = list(map(str, sys.argv[1].split(',')))
print(longestCommonPrefix(input))
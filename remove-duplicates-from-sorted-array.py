from typing import List
import sys

def removeDuplicates(nums: List[int]) -> int:
    pointer = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[pointer] = nums[i]
            pointer += 1

    return pointer

input = list(map(int, sys.argv[1].split(',')))
result = removeDuplicates(input)
print(result)
print(input)
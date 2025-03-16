from typing import List
import sys

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap.keys():
            return [hashmap[num], i]
        
        hashmap[target-num] = i

input = list(map(int, sys.argv[1].split(',')))
target = int(sys.argv[2])
print(twoSum(input, target))
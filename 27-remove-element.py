from typing import List


def removeElement(nums: List[int], val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


input = [2,3,6,5,0,0,4,7,8,9,6,0,2,1,45,8,9,6,4]
target = 0
val = removeElement(input, target)
print(val)
print(input)
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    size = len(nums)
    if size == 0:
        return 0
    if size == 1:
        if nums[0] == val:
            del nums[0]
            return 0
        return 1

    k = size - 1
    i = 0
    r = 0
    while i <= k:
        if nums[i] == val:
            while nums[i] == val and i < k:
                nums[i] = nums[k]
                nums[k] = val
                k -= 1
        if nums[i] != val:
            r += 1
        i += 1

    return r


input = [0,1,2,2,3,0,4,2]
target = 2
val = removeElement(input, target)
print(val)
print(input)
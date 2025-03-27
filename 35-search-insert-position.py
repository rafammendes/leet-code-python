from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    first_p = 0
    last_p = len(nums) - 1
    while True:
        if nums[first_p] == target:
            return first_p
        else:
            if nums[first_p] > target:
                return first_p
            first_p += 1
        if nums[last_p] == target:
            return last_p
        else:
            if nums[last_p] < target:
                return last_p + 1
            last_p -= 1


print(searchInsert([1,2,3,5,6,7], 4))
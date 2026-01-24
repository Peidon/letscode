from typing import List


def twoSum(nums: List[int], target_sum: int) -> List[int]:
    small, big = 0, len(nums) - 1
    while small < big:
        a = nums[small]
        b = nums[big]
        if target_sum == a + b:
            return [small+1, big+1]
        if target_sum > a + b:
            small += 1
        else:
            big -= 1

    return [small+1, big+1]


class Solution:
    pass

if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    lis = twoSum(numbers, target)
    print(lis)
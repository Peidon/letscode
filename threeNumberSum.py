from typing import List


class Solution:

    def __init__(self):
        self.func = _threeSum

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.func(nums)


def _threeSum(nums: List[int]) -> List[List[int]]:
    three = [List[int]] * 0

    nums.sort()
    d = {}

    for i, num in enumerate(nums):
        if num < 0:
            continue

        two = _twoSum(nums[:i], 0 - num)

        for t in two:

            if t[0] in d and d[t[0]] == t[1]:
                continue

            t.append(num)
            three.append(t)
            d[t[0]] = t[1]

    return three


def _twoSum(nums: List[int], target) -> List[List[int]]:
    if len(nums) < 2:
        return []

    d = {}  # num -> index
    two_list = [List[int]] * 0

    u = {}

    for i, num in enumerate(nums):

        if num in u:
            continue

        sub = target - num
        if sub in d:
            two_list.append([sub, num])
            u[num] = i
        d[num] = i

    return two_list


if __name__ == '__main__':
    res = _threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
    for lis in res:
        print(lis)

    res = _threeSum([-1, 0, 1, 2, -1, -4])
    for lis in res:
        print(lis)

    res = _threeSum([0, 0, 0, 0])
    for lis in res:
        print(lis)

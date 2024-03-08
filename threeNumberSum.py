from typing import List, Type


class Solution:

    def __init__(self):
        self.func = _threeSum

    def threeSum(self, nums: List[int]) -> List[Type[list]]:
        return self.func(nums)


def _threeSum(nums: List[int]) -> List[Type[list]]:
    three = [List[int]] * 0

    nums.sort()
    d = {}  # 用于去重

    for i, num in enumerate(nums):
        if num < 0:
            continue

        two = _twoSum(nums[:i], 0 - num)

        for t in two:

            if t[0] in d and d[t[0]] == t[1]:
                continue

            li = list(t)
            List.append(li, num)
            List.append(three, [li])

            d[t[0]] = t[1]

    return three


def _twoSum(nums: List[int], target) -> List[Type[list]]:
    if len(nums) < 2:
        return []

    two_list = [List[int]] * 0

    u = set()

    for i, num in enumerate(nums):

        if num in u:
            continue

        sub = target - num
        if sub in u:
            List.append(two_list, [sub, num])

        u.add(num)

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

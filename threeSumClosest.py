from typing import List


def _threeSumClosest(nums: List[int], target: int) -> int:
    if len(nums) < 3:
        return 0

    nums.sort()

    d = 1 << 32
    n = len(nums)

    closest = nums[0] + nums[1] + nums[2]

    for i, num in enumerate(nums):
        if i > 2 and num > target:
            break

        if i > 2 and num == nums[i - 1]:
            continue

        L = i + 1
        R = n - 1

        while L < R:
            s = num + nums[L] + nums[R]

            a = abs(target - s)
            if a < d:
                d = a
                closest = s

            # while L < R and nums[L + 1] == nums[L]:
            #     L += 1
            #
            # while L < R and nums[R - 1] == nums[R]:
            #     R -= 1

            if s == target:
                return s

            if s > target:
                R -= 1
            else:
                L += 1

    return closest


class Solution:
    def __init__(self):
        self.func = _threeSumClosest

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return self.func(nums, target)


if __name__ == '__main__':
    c = _threeSumClosest([-1000, -5, -5, -5, -5, -5, -5, -1, -1, -1], -14)
    print(c)

from typing import List


def jump(nums: List[int]) -> int:
    end = len(nums) - 1

    if end <= 0:
        return 0

    step = 0

    start = 0

    while start < end:
        step += 1
        start = _next_start(nums, start, end)

    return step


def _next_start(nums: List[int], i: int, tail: int) -> int:
    end = nums[i] + i
    if end >= tail:
        return tail

    m = 0
    right = end + 1

    for p in range(i + 1, right):
        d = p + nums[p]

        if d >= tail:
            return p

        if d > m and nums[p] != 0:
            m = d
            end = p

    return end


class Jumper(object):

    def __init__(self, a: [int]):
        if a is None:
            a = []
        self.position = 0
        self.step = 0
        self.road = a

    def to_end(self):
        a = self.road[self.position]
        if a + self.position >= len(self.road) - 1:
            return True
        return False

    def to_next_position(self):
        a = self.road[self.position]
        m = 0
        p = self.position
        for i in range(p+1, p+a+1):
            if i + self.road[i] > m:
                self.position = i
                m = i + self.road[i]
        self.step += 1

    def min_step(self):
        if self.position + 1 == len(self.road):
            return self.step
        return self.step + 1


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = Jumper(nums)
        while not j.to_end():
            j.to_next_position()
        return j.min_step()


if __name__ == '__main__':

    steps = Solution().jump([1,2,3])
    print(steps)

    steps = jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0])
    print(steps)

    steps = jump([3, 4, 3, 2, 5, 4, 3])
    assert steps == 3

    steps = jump([1, 1, 1, 1])
    assert steps == 3

    steps = jump([2, 3, 1, 1, 4])
    assert steps == 2

    steps = jump([2, 3, 0, 1, 4])
    assert steps == 2

    steps = jump([0])
    assert steps == 0

    steps = jump([1, 2])
    assert steps == 1

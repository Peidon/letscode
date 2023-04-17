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


if __name__ == '__main__':
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

from typing import List


class Jumper:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.farthest = 0   # farthest of a last jump
        self.pos = 0        # boundary(farthest+1) of last jump, start point to scan of new jump
        self.steps = 0

    def arrived_end(self) -> bool:
        return self.farthest >= len(self.array) - 1

    def next_jump(self):
        # scan items from current position to the farthest
        # update position, steps, farthest
        farthest = self.farthest
        for i in range(self.pos, self.farthest + 1):
            m = i + self.array[i]
            if m > farthest:
                farthest = m

        self.pos = self.farthest + 1
        self.steps += 1
        self.farthest = farthest



def jump_solution(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = Jumper(nums)
    while not j.arrived_end():
        j.next_jump()
    return j.steps


if __name__ == '__main__':

    steps = jump_solution([1,2,3])
    print(steps)

    steps = jump_solution([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0])
    print(steps)

    steps = jump_solution([3, 4, 3, 2, 5, 4, 3])
    assert steps == 3

    steps = jump_solution([1, 1, 1, 1])
    assert steps == 3

    steps = jump_solution([2, 3, 1, 1, 4])
    assert steps == 2

    steps = jump_solution([2, 3, 0, 1, 4])
    assert steps == 2

    steps = jump_solution([0])
    assert steps == 0

    steps = jump_solution([1, 2])
    assert steps == 1

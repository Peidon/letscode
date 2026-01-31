from typing import List


def create_pivot(a: List[int], l: int, r: int) -> int:
    pivot = a[l]
    while l < r:
        while l < r and pivot <= a[r]:
            r -= 1
        a[l] = a[r]

        while l < r and a[l] <= pivot:
            l += 1
        a[r] = a[l]

    a[l] = pivot
    return l


def majorityElement(nums: List[int]) -> int:
    """
    # The majority element is the element that appears more than ⌊n / 2⌋ times.
    # You may assume that the majority element always exists in the array.
    """

    l, r = 0, len(nums) - 1
    d = len(nums) // 2

    while l < r:
        p = create_pivot(nums, l, r)
        if p > d:
            r = p - 1
        elif p < d:
            l = p + 1
        else:
            return nums[p]

    return nums[l]


if __name__ == '__main__':
    m = majorityElement([3,3,4])
    print(m)
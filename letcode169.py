from typing import List


class Solution:

    def create_pivot(self, a: List[int], l: int, r: int) -> int:
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

    def majorityElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        d = len(nums) // 2

        while l < r:
            p = self.create_pivot(nums, l, r)
            if p > d:
                r = p - 1
            elif p < d:
                l = p + 1
            else:
                return nums[p]

        return nums[l]


if __name__ == '__main__':
    s = Solution()
    m = s.majorityElement([3,3,4])
    print(m)
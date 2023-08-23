from typing import List, Type


class Solution:

    def __init__(self):
        self.candidates = []
        self.n = 0
        self.ans = []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        self.candidates = nums
        self.n = len(nums)

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tri = self._threeSum(i + 1, target - num)
            for lis in tri:
                lis.append(num)
                self.ans.append(lis)

        return self.ans

    def _threeSum(self, offset: int, target: int) -> List[Type[list]]:

        a, b, c = offset, offset + 1, offset + 2

        if c >= self.n:
            return []

        if self.candidates[a] + self.candidates[b] + self.candidates[c] > target:
            return []

        ans = [List[int]] * 0

        for i in range(a, self.n):

            if self.candidates[i] > target and self.candidates[i] > 0:
                break

            if i > a and self.candidates[i] == self.candidates[i - 1]:
                continue

            L = i + 1
            R = self.n - 1

            while L < R:

                if L > i + 1 and self.candidates[L] == self.candidates[L - 1]:
                    L += 1
                    continue

                ca = self.candidates[i] + self.candidates[L] + self.candidates[R]

                if ca == target:
                    ans.append([self.candidates[i], self.candidates[L], self.candidates[R]])

                if self.candidates[i] + self.candidates[L] + self.candidates[R] > target:
                    R -= 1
                else:
                    L += 1

        return ans


if __name__ == '__main__':
    so = Solution()
    so.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11)
    print(so.ans)

class Solution:

    def __init__(self):
        self.idx = dict()
        self.sum = 0

    def _exists(self, num: int):
        if num in self.idx and self.idx[num] >= 0:
            return True
        return False

    def _add_num_to_window(self, num: int, i: int):
        self.idx[num] = i
        self.sum += num

    def _move_forward(self, nums: list[int], old_start: int):
        num = nums[old_start]
        self.idx[num] = -1
        self.sum -= num
        return old_start + 1

    def _remove_range(self, nums: list[int], start: int, end: int):
        for i in range(start, end):
            self.idx[nums[i]] = -1
            self.sum -= nums[i]

    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        start = 0

        for cur in range(len(nums)):

            num = nums[cur]

            if self._exists(num):
                # update window
                # move start forward to current point
                new_start = self.idx[num] + 1
                self._remove_range(nums, start, new_start)
                start = new_start

            self._add_num_to_window(num, cur)

            # k is the length of the window, so (k-1 + start) is the end of window
            if (start + k - 1) == cur:
                result = max(result, self.sum)
                start = self._move_forward(nums, start)

        return result

if __name__ == '__main__':
    ans = Solution().maximumSubarraySum([4], 1)
    print(ans)
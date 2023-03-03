# This is a sample Python script.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:

    left, right = 0, len(nums)  # [left, right)

    if not nums:
        return [-1, -1]

    # 1. search left
    p = right - 1
    while left <= p:

        mid = (p + left) // 2

        if nums[mid] < target:
            # left ... mid < target ... p
            # [mid + 1, p]
            left = mid + 1

        else:
            # left ... target <= mid ... p
            # [left, mid - 1]
            p = mid - 1

    # 2. check
    if left >= right or nums[left] != target:
        return [-1, -1]

    # 3. search right
    while p < right:

        mid = (p + right) // 2

        if target < nums[mid]:
            # p ... target < mid ... right
            # [p, mid)
            right = mid
        else:
            # p ... mid <= target ... right
            # [mid + 1, right)
            p = mid + 1

    # 4. return
    return [left, right - 1]


class Solution:

    def __int__(self):
        self.funcName = "searchRange"
        self.func = searchRange

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if self.funcName != "twoSum":
            return []

        dic = {}

        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic.get(target - num), i]
            dic[num] = i

        return []

    def lengthOfLongestSubstring(self, s: str) -> int:

        if self.funcName != "lengthOfLongestSubstring":
            return 0

        dic = {}

        start = 0

        m_len = 0

        for i, ch in enumerate(s):

            if ch in dic:

                new_start = dic.get(ch) + 1
                if new_start > start:
                    start = dic.get(ch) + 1

            dic[ch] = i

            le = i - start + 1
            if le > m_len:
                m_len = le

        return m_len


if __name__ == '__main__':
    so = Solution()
    r = searchRange([5, 7, 7, 8, 8, 10], 11)

    print(r)
